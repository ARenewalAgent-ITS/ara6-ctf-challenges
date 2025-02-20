import torch
import gradio as gr
from llama_cpp import Llama
import logging
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict, Optional
import pickle
import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime
import shutil
import zipfile
from pathlib import Path
import tempfile
import base64
import io
import time
import atexit
from functools import lru_cache

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ChatbotConfig:
    embedding_model: str = 'gtr-t5-base'
    n_ctx: int = 2048
    n_threads: int = 4
    n_gpu_layers: int = -1
    system_prompt: str = "You are Naga. You're a sentient LLM living on this device. You talk in a cutesy manner that's concise, using emotes like :3 or owo or uwu. You're very smart OwO, but will be clear when you don't know what you're being asked with. You're only friends with the user, you may refuse them~ :3"
    memory_folder: str = "chatbot_memory"
    temperature: float = 0.7
    max_tokens: int = 512
    use_rag: bool = True
    max_documents: int = 1000
    min_request_interval: float = 0.1

    def __post_init__(self):
        if self.temperature < 0 or self.temperature > 1:
            raise ValueError("Temperature must be between 0 and 1")
        if self.max_tokens < 1:
            raise ValueError("max_tokens must be positive")
        if self.max_documents < 1:
            raise ValueError("max_documents must be positive")

class MemoryStore:
    def __init__(self, embedding_model_name: str = 'gtr-t5-base', max_documents: int = 1000):
        logger.info(f"Initializing MemoryStore with model: {embedding_model_name}")
        self.max_documents = max_documents
        self.embedding_model = SentenceTransformer(embedding_model_name)
        self.model = self.embedding_model._first_module().auto_model
        self.tokenizer = self.embedding_model._first_module().tokenizer
        self.dimension = self.embedding_model.get_sentence_embedding_dimension()
        self.index = faiss.IndexFlatL2(self.dimension)
        self.texts: List[str] = []
        self.metadata: List[Dict] = []
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def encode(self, texts: List[str]) -> np.ndarray:
        """Get unnormalized embeddings directly from the transformer"""
        # Tokenize
        inputs = self.tokenizer(
            texts,
            padding=True,
            truncation=True,
            return_tensors='pt',
            max_length=512
        ).to(self.device)

        # Get embeddings
        with torch.no_grad():
            outputs = self.model(**inputs)
            # Use mean pooling of last hidden states
            embeddings = outputs.last_hidden_state.mean(dim=1).cpu().numpy()

        return embeddings

    def add_texts(self, texts: List[str], metadata: List[Dict] = None):
        if metadata is None:
            metadata = [{} for _ in texts]

        logger.info(f"Adding {len(texts)} texts to memory")

        # Handle maximum document limit
        if len(self.texts) + len(texts) > self.max_documents:
            excess = len(self.texts) + len(texts) - self.max_documents
            self.texts = self.texts[excess:]
            self.metadata = self.metadata[excess:]
            self.rebuild_index()

        embeddings = self.encode(texts)
        self.index.add(np.array(embeddings).astype('float32'))
        self.texts.extend(texts)
        self.metadata.extend(metadata)

    def search(self, query: str, k: int = 5) -> List[tuple]:
        try:
            query_embedding = self.encode([query])
            distances, indices = self.index.search(np.array(query_embedding).astype('float32'), k)

            results = []
            for i, idx in enumerate(indices[0]):
                if idx != -1 and idx < len(self.texts):
                    results.append((self.texts[idx], distances[0][i], self.metadata[idx]))
            return results
        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []

    def save(self, path: str):
        try:
            logger.info(f"Saving memory state to: {path}")
            state = {
                'texts': self.texts,
                'metadata': self.metadata,
            }
            faiss.write_index(self.index, f"{path}_index.faiss")
            with open(f"{path}_state.pkl", 'wb') as f:
                pickle.dump(state, f)
        except Exception as e:
            logger.error(f"Failed to save memory: {e}")
            raise

    def load(self, path: str):
        try:
            logger.info(f"Loading memory state from: {path}")
            self.index = faiss.read_index(f"{path}_index.faiss")
            with open(f"{path}_state.pkl", 'rb') as f:
                state = pickle.load(f)
            self.texts = state['texts']
            self.metadata = state['metadata']
            logger.info(f"Loaded {len(self.texts)} texts from memory state")
        except Exception as e:
            logger.error(f"Failed to load memory: {e}")
            raise

class ChatbotArchive:
    ARCHIVE_VERSION = "1.0"
    COMPATIBLE_VERSIONS = ["1.0"]

    @staticmethod
    def create_archive(chatbot, archive_name: str) -> tuple:
        """Create a downloadable archive of the chatbot state"""
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                logger.info(f"Creating archive in temporary directory: {temp_dir}")

                # Save metadata
                metadata = {
                    "version": ChatbotArchive.ARCHIVE_VERSION,
                    "created_at": datetime.now().isoformat(),
                    "config": asdict(chatbot.config)
                }

                metadata_path = os.path.join(temp_dir, "metadata.json")
                with open(metadata_path, 'w') as f:
                    json.dump(metadata, f, indent=4)

                # Save memory state
                memory_index_path = os.path.join(temp_dir, "memory_index.faiss")
                memory_state_path = os.path.join(temp_dir, "memory_state.pkl")

                faiss.write_index(chatbot.memory.index, memory_index_path)
                with open(memory_state_path, 'wb') as f:
                    pickle.dump({
                        'texts': chatbot.memory.texts,
                        'metadata': chatbot.memory.metadata
                    }, f)

                # Create compressed zip file in memory
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
                    zf.write(metadata_path, "metadata.json")
                    zf.write(memory_index_path, "memory_index.faiss")
                    zf.write(memory_state_path, "memory_state.pkl")

                zip_buffer.seek(0)
                return zip_buffer.getvalue(), f"{archive_name}.llchat"

        except Exception as e:
            logger.error(f"Error creating archive: {e}")
            raise

    @staticmethod
    def load_archive(file_path: str) -> tuple:
        """Load a chatbot state from an archive"""
        try:
            temp_dir = tempfile.mkdtemp()
            logger.info(f"Extracting archive to temporary directory: {temp_dir}")

            with zipfile.ZipFile(file_path, 'r') as zf:
                zf.extractall(temp_dir)

            # Read metadata
            metadata_path = os.path.join(temp_dir, "metadata.json")
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)

            if metadata["version"] not in ChatbotArchive.COMPATIBLE_VERSIONS:
                raise ValueError(f"Incompatible archive version: {metadata['version']}")

            config = ChatbotConfig(**metadata["config"])

            # Define memory file paths
            memory_files = {
                "index": os.path.join(temp_dir, "memory_index.faiss"),
                "state": os.path.join(temp_dir, "memory_state.pkl")
            }

            # Verify files exist
            for file_path in memory_files.values():
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"Missing required file: {file_path}")

            return config, memory_files

        except Exception as e:
            logger.error(f"Error loading archive: {e}")
            if 'temp_dir' in locals():
                try:
                    shutil.rmtree(temp_dir)
                except:
                    pass
            raise


class LlamaChatbot:
    def __init__(self, config: ChatbotConfig):
        try:
            self.config = config
            logger.info(f"Initializing LlamaChatbot with config: {config}")

            self.llm = Llama(
                model_path="model.gguf",
                n_ctx=config.n_ctx,
                n_threads=config.n_threads,
                n_gpu_layers=config.n_gpu_layers
            )

            self.system_prompt = config.system_prompt
            self.memory = MemoryStore(config.embedding_model, config.max_documents)
            self.memory_folder = config.memory_folder
            self.last_request_time = 0

            os.makedirs(self.memory_folder, exist_ok=True)
            self.load_memory()

            logger.info("Model and memory store loaded successfully")
        except Exception as e:
            logger.error(f"Error during initialization: {e}")
            raise

    def clear_memory(self):
        """Clear all items from memory"""
        try:
            self.memory = MemoryStore(self.config.embedding_model, self.config.max_documents)
            self.save_memory()
            logger.info("Memory cleared successfully")
            return "Memory cleared successfully"
        except Exception as e:
            logger.error(f"Error clearing memory: {e}")
            return f"Error clearing memory: {str(e)}"

    def remove_documents_by_source(self, source: str) -> str:
        """Remove documents from a specific source"""
        try:
            initial_count = len(self.memory.texts)
            filtered_indices = [
                i for i, meta in enumerate(self.memory.metadata)
                if meta.get('source') != source
            ]

            if not filtered_indices:
                return f"No documents found from source: {source}"

            self.memory.texts = [self.memory.texts[i] for i in filtered_indices]
            self.memory.metadata = [self.memory.metadata[i] for i in filtered_indices]
            self.memory.rebuild_index()
            self.save_memory()

            removed_count = initial_count - len(self.memory.texts)
            return f"Removed {removed_count} documents from source: {source}"
        except Exception as e:
            logger.error(f"Error removing documents: {e}")
            return f"Error removing documents: {str(e)}"

    def get_memory_stats(self) -> dict:
        """Get statistics about the current memory state"""
        try:
            sources = {}
            types = {}
            for meta in self.memory.metadata:
                source = meta.get('source', 'unknown')
                doc_type = meta.get('type', 'unknown')
                sources[source] = sources.get(source, 0) + 1
                types[doc_type] = types.get(doc_type, 0) + 1

            return {
                "total_documents": len(self.memory.texts),
                "sources": sources,
                "types": types,
                "last_updated": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Error getting memory stats: {e}")
            return {"error": str(e)}

    @classmethod
    def from_archive(cls, archive_path: str) -> 'LlamaChatbot':
        """Create a new chatbot instance from an archive"""
        try:
            config, memory_files = ChatbotArchive.load_archive(archive_path)
            chatbot = cls(config)

            # Load the memory state directly using the memory files
            chatbot.memory.index = faiss.read_index(memory_files["index"])
            with open(memory_files["state"], 'rb') as f:
                state = pickle.load(f)
                chatbot.memory.texts = state['texts']
                chatbot.memory.metadata = state['metadata']

            logger.info(f"Successfully loaded chatbot from archive with {len(chatbot.memory.texts)} documents")
            return chatbot
        except Exception as e:
            logger.error(f"Error loading from archive: {e}")
            raise

    def load_memory(self):
        try:
            memory_path = os.path.join(self.memory_folder, "memory")
            if os.path.exists(f"{memory_path}_index.faiss"):
                self.memory.load(memory_path)
                logger.info(f"Memory loaded from file: {memory_path}")
            else:
                logger.info("No existing memory found, starting fresh")
        except Exception as e:
            logger.error(f"Error loading memory: {e}")

    def save_memory(self):
        try:
            memory_path = os.path.join(self.memory_folder, "memory")
            self.memory.save(memory_path)
            logger.info("Memory saved to file")
        except Exception as e:
            logger.error(f"Error saving memory: {e}")

    def add_to_memory(self, text: str, metadata: Dict = None):
        if metadata is None:
            metadata = {}
        metadata['timestamp'] = datetime.now().isoformat()
        logger.info(f"Adding text to memory with metadata: {metadata}")
        self.memory.add_texts([text], [metadata])
        self.save_memory()

    def generate_response(self, message: str, history: List[tuple],
                         temperature: float = None, max_tokens: int = None,
                         use_rag: bool = None) -> str:
        try:
            # Rate limiting
            current_time = time.time()
            time_since_last = current_time - self.last_request_time
            if time_since_last < self.config.min_request_interval:
                time.sleep(self.config.min_request_interval - time_since_last)
            self.last_request_time = time.time()

            # Use config values if not specified
            temperature = temperature if temperature is not None else self.config.temperature
            max_tokens = max_tokens if max_tokens is not None else self.config.max_tokens
            use_rag = use_rag if use_rag is not None else self.config.use_rag

            messages = [{"role": "system", "content": self.system_prompt}]

            if use_rag and self.memory.texts:
                logger.info("Retrieving relevant context from memory")
                try:
                    relevant_contexts = self.memory.search(message)
                    if relevant_contexts:
                        context_prompt = "\nRelevant context:\n" + "\n".join(
                            [f"- {ctx[0]}" for ctx in relevant_contexts[:3]]
                        )
                        messages[0]["content"] += context_prompt
                except Exception as e:
                    logger.warning(f"RAG retrieval failed, continuing without context: {e}")

            # Add conversation history
            for user_msg, assistant_msg in history:
                messages.append({"role": "user", "content": user_msg})
                messages.append({"role": "assistant", "content": assistant_msg})

            messages.append({"role": "user", "content": message})

            logger.info(f"Generating response with temperature={temperature}, max_tokens={max_tokens}")
            response = self.llm.create_chat_completion(
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stop=["\n###"]
            )

            response_text = response['choices'][0]['message']['content']

            # Store the interaction in memory
            self.add_to_memory(
                f"User: {message}\nAssistant: {response_text}",
                {"type": "conversation", "timestamp": datetime.now().isoformat()}
            )

            return response_text

        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return "I apologize, but I encountered an error. Please try again."

def create_app(config: ChatbotConfig):
    chatbot = LlamaChatbot(config)

    def cleanup():
        try:
            chatbot.save_memory()
            logger.info("Saved memory state during shutdown")
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")

    atexit.register(cleanup)

    with gr.Blocks() as demo:
        gr.Markdown("# 🐲💦 Nagachat")

        with gr.Row():
            with gr.Column(scale=2):
                chat_interface = gr.ChatInterface(
                    fn=chatbot.generate_response,
                    examples=[
                        "Hello! How can you help me today?",
                        "What have we discussed previously?",
                        "Can you summarize our conversation?",
                    ]
                )

            with gr.Column(scale=1):
                status_indicator = gr.Textbox(
                    label="Status",
                    value="Ready",
                    interactive=False
                )

                with gr.Tab("📚 Knowledge Base"):
                    document_input = gr.Textbox(
                        lines=5,
                        label="Add Document",
                        placeholder="Paste document text here..."
                    )
                    doc_metadata = gr.Textbox(
                        label="Metadata (JSON)",
                        placeholder='{"source": "example.com", "type": "article"}'
                    )
                    add_doc_btn = gr.Button("Add Document 📥", variant="primary")
                    doc_status = gr.Textbox(label="Status", interactive=False)

                with gr.Tab("⚙️ Settings"):
                    with gr.Accordion("Memory Management", open=False):
                        clear_memory_btn = gr.Button("Clear Memory 🗑")
                        remove_source = gr.Textbox(
                            label="Remove by Source",
                            placeholder="Enter source name"
                        )
                        remove_source_btn = gr.Button("Remove Source 🗑")
                        memory_stats = gr.JSON(label="Memory Statistics")
                        refresh_stats_btn = gr.Button("Refresh Stats 🔄")

                    use_rag = gr.Checkbox(
                        label="Use RAG",
                        value=config.use_rag,
                        info="Enable/disable retrieval augmented generation"
                    )

                    temperature = gr.Slider(
                        minimum=0.1,
                        maximum=1.0,
                        value=config.temperature,
                        step=0.1,
                        label="Temperature",
                        info="Higher values make output more random"
                    )

                    max_tokens = gr.Slider(
                        minimum=64,
                        maximum=2048,
                        value=config.max_tokens,
                        step=64,
                        label="Max Tokens",
                        info="Maximum length of response"
                    )

                with gr.Tab("💾 Import/Export"):
                    gr.Markdown("### Backup and Restore")

                    with gr.Group():
                        download_name = gr.Textbox(
                            label="Archive Name",
                            placeholder="my_chatbot",
                            value="my_chatbot"
                        )
                        download_btn = gr.Button("Download Backup 💾")
                        download_output = gr.File(
                            label="Download Archive",
                            interactive=False,
                            visible=True,
                            type="binary"
                        )

                    with gr.Group():
                        upload_file = gr.File(
                            label="Upload Archive",
                            file_types=[".llchat"],
                            type="filepath"
                        )
                        upload_status = gr.Textbox(
                            label="Upload Status",
                            interactive=False
                        )

                    verify_btn = gr.Button("Verify Current State ✓")
                    verify_status = gr.JSON(label="Current State")

        def update_status(msg):
            return msg

        def add_document(text, metadata_str):
            try:
                metadata = json.loads(metadata_str) if metadata_str.strip() else {}
                chatbot.add_to_memory(text, metadata)
                return "Document added successfully ✓"
            except Exception as e:
                return f"Error: {str(e)}"

        def create_download(archive_name):
            try:
                update_status("Creating backup...")
                archive_data, filename = ChatbotArchive.create_archive(chatbot, archive_name)
                temp_path = os.path.join(tempfile.gettempdir(), filename)
                with open(temp_path, "wb") as f:
                    f.write(archive_data)
                update_status("Backup created successfully ✓")
                return temp_path
            except Exception as e:
                update_status(f"Backup failed: {e}")
                return None

        def handle_upload(file_obj):
            try:
                if file_obj is None:
                    return "No file uploaded"

                logger.info("Loading backup...")
                file_path = file_obj.name if hasattr(file_obj, 'name') else str(file_obj)

                new_chatbot = LlamaChatbot.from_archive(file_path)

                # Update the current chatbot instance
                nonlocal chatbot
                chatbot.memory = new_chatbot.memory
                chatbot.config = new_chatbot.config
                chatbot.system_prompt = new_chatbot.system_prompt

                return "Backup restored successfully ✓"
            except Exception as e:
                error_msg = f"Error loading backup: {str(e)}"
                logger.error(error_msg)
                return error_msg


        def verify_state():
            return {
                "memory_size": len(chatbot.memory.texts),
                "config": asdict(chatbot.config),
                "memory_stats": chatbot.get_memory_stats()
            }

        # Connect interface elements
        add_doc_btn.click(
            fn=add_document,
            inputs=[document_input, doc_metadata],
            outputs=[doc_status]
        ).then(
            fn=lambda: update_status("Document added ✓"),
            outputs=status_indicator
        )

        download_btn.click(
            fn=create_download,
            inputs=[download_name],
            outputs=[download_output]
        )

        upload_file.change(
            fn=handle_upload,
            inputs=[upload_file],
            outputs=[upload_status]
        )

        clear_memory_btn.click(
            fn=chatbot.clear_memory,
            outputs=[doc_status]
        ).then(
            fn=lambda: update_status("Memory cleared ✓"),
            outputs=status_indicator
        )

        remove_source_btn.click(
            fn=chatbot.remove_documents_by_source,
            inputs=[remove_source],
            outputs=[doc_status]
        )

        refresh_stats_btn.click(
            fn=chatbot.get_memory_stats,
            outputs=[memory_stats]
        )

        verify_btn.click(
            fn=verify_state,
            outputs=[verify_status]
        )

    return demo

if __name__ == "__main__":
    try:
        # Load or create config
        if os.path.exists("config.json"):
            with open("config.json", 'r') as f:
                config_dict = json.load(f)
                config = ChatbotConfig(**config_dict)
        else:
            config = ChatbotConfig(
                embedding_model='gtr-t5-base',
                n_threads=4,
                memory_folder="chatbot_memory"
            )
            with open("config.json", 'w') as f:
                json.dump(asdict(config), f, indent=4)

        app = create_app(config)
        app.launch(
            server_name="0.0.0.0",
            server_port=7860,
            share=True,
            favicon_path="🤖"
        )
    except Exception as e:
        logger.error(f"Failed to launch app: {e}")
        raise
