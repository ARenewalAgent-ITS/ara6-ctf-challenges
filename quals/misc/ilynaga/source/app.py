import gradio as gr
from deepface import DeepFace
import torch
import numpy as np
from PIL import Image
import random
from skimage.metrics import structural_similarity as ssim
import tensorflow as tf
import requests
import os
import transformers

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    transformers.set_seed(seed)
    tf.random.set_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)

flag = os.environ["FLAG"] if "FLAG" in os.environ else "fakeflag{placeholder}"

ssim_reference_url = "https://files.catbox.moe/b6p5fj.png"
face_reference_url = "https://files.catbox.moe/m0g0ek.png"
ssim_reference_path = "ssim_reference.png"
face_reference_path = "face_reference.png"

# Download SSIM reference
if not os.path.exists(ssim_reference_path):
    response = requests.get(ssim_reference_url)
    with open(ssim_reference_path, "wb") as f:
        f.write(response.content)

# Download face verification reference
if not os.path.exists(face_reference_path):
    response = requests.get(face_reference_url)
    with open(face_reference_path, "wb") as f:
        f.write(response.content)

ssim_reference = Image.open(ssim_reference_path)

def compare_face_ssim(img1, img2, face_area):
    # Convert PIL images to numpy arrays if needed
    if isinstance(img1, Image.Image):
        img1 = np.array(img1)
    if isinstance(img2, Image.Image):
        img2 = np.array(img2)
    
    # Ensure both images are RGB (3 channels)
    if img1.shape[-1] == 4:
        img1 = img1[:,:,:3]
    if img2.shape[-1] == 4:
        img2 = img2[:,:,:3]
    
    # Extract face regions
    x, y, w, h = face_area['x'], face_area['y'], face_area['w'], face_area['h']
    face1 = img1[y:y+h, x:x+w]
    face2 = img2[y:y+h, x:x+w]
    
    # Convert to float32 if needed
    if face1.dtype != np.float32:
        face1 = face1.astype(np.float32) / 255.0
    if face2.dtype != np.float32:
        face2 = face2.astype(np.float32) / 255.0
    
    # Calculate multichannel SSIM
    ssim_value = ssim(face1, face2, data_range=1.0, channel_axis=2, win_size=3)
    return ssim_value

def predict_and_compare(image):
    # Save uploaded image temporarily
    temp_path = "temp_upload.png"
    image.save(temp_path)
    
    try:
        # Run DeepFace verification against face reference
        result = DeepFace.verify(temp_path, face_reference_path)
        verified = result["verified"]
        distance = result["distance"]
        
        # Get face area for SSIM
        face_area = DeepFace.extract_faces(temp_path)[0]["facial_area"]
        
        # Calculate SSIM against SSIM reference
        ssim_value = compare_face_ssim(image, ssim_reference, face_area)
        
        predicted_class = "True" if verified else "False"
        probability = 1 - abs(distance)

        success = f"""
<div style="font-family: 'Courier New', monospace; background: #1a1b26; color: #a9b1d6; padding: 20px; border-radius: 8px;">
    <span style="color: #7aa2f7">guest@terminal</span>:<span style="color: #9ece6a">~</span>$ ssh jerry@husseumi.space<br>
    Connecting to husseumi.space on port 22...<br><br>
    
    <span style="color: #bb9af7">✧ Initiating facial authentication... ✧</span><br>
    <span style="color: #7dcfff">⋆｡°✩ Scanning face... ✩°｡⋆</span><br>
    <span style="color: #7dcfff">.｡*ﾟ Matching with database... ﾟ*｡.</span><br>
    <span style="color: #9ece6a">✧･ﾟ: Biometric verification complete! :･ﾟ✧</span><br><br>
    
    <div style="background: #1f2335; padding: 10px; border-radius: 4px; margin: 10px 0;">
    <pre style="color: #7aa2f7; margin: 0; font-family: monospace;">
╭──── 🌠 Welcome to Jelly's Space 🌠 ─────╮
│   *:･ﾟ✧ Authentication successful! ✧ﾟ･:*  |
│         a-awawawa... welcome back!        │
╰─────────────- ✧◝(⁰▿⁰)◜✧ -────────────╯</pre>
    </div>

    Last login: Wed Mar 13 12:34:56 2024 from 192.168.1.1<br>
    <span style="color: #bb9af7">This server is powered by dewaweb™ - Empowering Your Digital Dreams ⋆｡°✩</span><br><br>
    
    <span style="color: #7aa2f7">jerry@husseumi</span>:<span style="color: #9ece6a">~</span>$ cat ~/.auth/metrics.log<br>
    <span style="color: #7dcfff">⭑⋆˙⟡ Facial Match   : {predicted_class}</span><br>
    <span style="color: #7dcfff">⭑⋆˙⟡ Match Score    : {probability:.4f}</span><br>
    <span style="color: #7dcfff">⭑⋆˙⟡ Similarity     : {ssim_value:.4f}</span><br><br>
    
    <span style="color: #7aa2f7">jerry@husseumi</span>:<span style="color: #9ece6a">~</span>$ sudo cat /etc/secrets/flag.txt<br>
    <span style="color: #f7768e">⋆｡°✩ {flag} ✩°｡⋆</span><br><br>
    
    <span style="color: #7aa2f7">jerry@husseumi</span>:<span style="color: #9ece6a">~</span>$ exit<br>
    <span style="color: #bb9af7">✧･ﾟ: A-awawawa... goodbye! Have a lovely day! :･ﾟ✧</span><br>
    <span style="color: #bb9af7">.｡*ﾟ+.*.｡(っ°v°c)｡.*+.ﾟ*｡.</span><br><br>
    
    Connection to husseumi.space closed.
</div>
"""

        fail = f"""
<div style="font-family: 'Courier New', monospace; background: #1a1b26; color: #a9b1d6; padding: 20px; border-radius: 8px;">
    <span style="color: #7aa2f7">guest@terminal</span>:<span style="color: #9ece6a">~</span>$ ssh jerry@husseumi.space<br>
    Connecting to husseumi.space on port 22...<br><br>
    
    <span style="color: #bb9af7">✧ Initiating facial authentication... ✧</span><br>
    <span style="color: #7dcfff">⋆｡°✩ Scanning face... ✩°｡⋆</span><br>
    <span style="color: #7dcfff">.｡*ﾟ Matching with database... ﾟ*｡.</span><br>
    <span style="color: #f7768e">(◞‸◟；) Biometric verification failed</span><br><br>
    
    Authentication Report:<br>
    <span style="color: #7dcfff">｡･ﾟﾟ･ Face Match    : {predicted_class}</span><br>
    <span style="color: #7dcfff">｡･ﾟﾟ･ Match Score   : {probability:.4f}</span><br>
    <span style="color: #7dcfff">｡･ﾟﾟ･ Similarity    : {ssim_value:.4f}</span><br><br>
    
    <span style="color: #f7768e">Permission denied (publickey,facial).</span><br>
    Connection to husseumi.space closed.
</div>
"""
        return success if ssim_value>=0.96 and predicted_class == 'True' else fail
        
    finally:
        # Cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)

custom_css = """
#output-html {
    font-family: 'Courier New', monospace;
    background: #1a1b26;
    color: #a9b1d6;
    padding: 20px;
    border-radius: 8px;
    min-height: 200px;
    margin-top: 10px;
}
"""

default_output = """
<div style="font-family: 'Courier New', monospace; background: #1a1b26; color: #a9b1d6; padding: 20px; border-radius: 8px;">
    <span style="color: #7aa2f7">guest@terminal</span>:<span style="color: #9ece6a">~</span>$ ssh jerry@husseumi.space<br>
    <span style="color: #7dcfff">Awaiting facial authentication...</span><br>
    <span style="color: #bb9af7">Please submit an image to proceed ˚ ༘ ೀ⋆｡˚</span>
</div>
"""

iface = gr.Interface(
    fn=predict_and_compare,
    inputs=gr.Image(type="pil", label="Upload Image"),
    outputs=gr.HTML(value=default_output),
    title="Jelly's Authentication System 🌠",
    description="Submit your image to authenticate!",
    allow_flagging="never",
    css=custom_css,
    theme="allenai/gradio-theme"
)

iface.queue()
iface.launch(show_api=False)