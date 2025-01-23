import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from deepface import DeepFace
from deepface.models.facial_recognition import VGGFace
from tqdm import tqdm
from skimage.metrics import structural_similarity as ssim
import tensorflow as tf


# Utility functions
def cosine_similarity(x, y):
    return tf.reduce_sum(x * y) / (tf.norm(x) * tf.norm(y))


def cosine_distance(x, y):
    return 1 - cosine_similarity(x, y)


def get_vgg_model():
    model = VGGFace.load_model()
    embedding_layer = model.layers[-5].name
    return tf.keras.Model(
        inputs=model.input, outputs=model.get_layer(embedding_layer).output
    )


def extract_face(image, face_area):
    x, y, w, h = face_area["x"], face_area["y"], face_area["w"], face_area["h"]
    image = np.array(image)
    return image[y : y + h, x : x + w, :]


# Pastes at the area from perturbed to original
def paste_face(original_img, perturbed_face, face_area):
    result = np.array(original_img.copy())
    x, y, w, h = face_area["x"], face_area["y"], face_area["w"], face_area["h"]
    perturbed_face = cv2.resize(perturbed_face, (w, h))

    if perturbed_face.dtype != np.uint8:
        perturbed_face = (perturbed_face * 255).astype(np.uint8)

    result[y : y + h, x : x + w, :3] = perturbed_face
    return result


def attack(image, target_image, epsilon=0.1, alpha=0.01, steps=10):
    model = get_vgg_model()

    # Preprocess images
    image = image[:, :, :3] if image.shape[-1] == 4 else image  # Ensure RGB bleh
    target_image = (
        target_image[:, :, :3] if target_image.shape[-1] == 4 else target_image
    )

    image = image.astype("float32") / 255.0 if image.dtype != np.float32 else image
    target_image = (
        target_image.astype("float32") / 255.0
        if target_image.dtype != np.float32
        else target_image
    )

    image = cv2.resize(image, (224, 224))
    target_image = cv2.resize(target_image, (224, 224))
    original = image.copy()

    perturbed = tf.convert_to_tensor(image, dtype=tf.float32)
    perturbed = tf.expand_dims(perturbed, 0)
    target = tf.convert_to_tensor(target_image, dtype=tf.float32)
    target = tf.expand_dims(target, 0)

    target_embedding = model(target)

    for _ in tqdm(range(steps)):
        with tf.GradientTape() as tape:
            tape.watch(perturbed)
            current_embedding = model(perturbed)
            loss = -cosine_distance(current_embedding, target_embedding)

        gradients = tape.gradient(loss, perturbed)
        grad_norm = tf.norm(gradients)
        normalized_gradients = gradients / (grad_norm + 1e-8)
        perturbed = perturbed + alpha * normalized_gradients

        delta = perturbed - tf.convert_to_tensor(original, dtype=tf.float32)
        norm = tf.norm(delta)
        delta = epsilon * delta / tf.maximum(epsilon, norm)
        perturbed = tf.convert_to_tensor(original, dtype=tf.float32) + delta
        perturbed = tf.clip_by_value(perturbed, 0, 1)

    return perturbed.numpy()[0]


def compare_face_ssim(img1, img2, face_area):
    # Convert and preprocess images
    img1 = np.array(img1) if isinstance(img1, Image.Image) else img1
    img2 = np.array(img2) if isinstance(img2, Image.Image) else img2

    img1 = img1[:, :, :3] if img1.shape[-1] == 4 else img1
    img2 = img2[:, :, :3] if img2.shape[-1] == 4 else img2

    # Extract faces
    x, y, w, h = face_area["x"], face_area["y"], face_area["w"], face_area["h"]
    face1 = img1[y : y + h, x : x + w]
    face2 = img2[y : y + h, x : x + w]

    face1 = face1.astype(np.float32) / 255.0
    face2 = face2.astype(np.float32) / 255.0

    return np.mean(
        [ssim(face1[:, :, i], face2[:, :, i], data_range=1.0) for i in range(3)]
    )


def visualize_results(original, perturbed, target):
    plt.figure(figsize=(15, 5))

    plt.subplot(131)
    plt.imshow(original)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(132)
    plt.imshow(perturbed)
    plt.title("Perturbed")
    plt.axis("off")

    plt.subplot(133)
    plt.imshow(target)
    plt.title("Target")
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    # Load and process images
    face_info = DeepFace.extract_faces("nagaluv.png")[0]
    target_info = DeepFace.extract_faces("oshiluv.png")[0]

    aligned_img = extract_face(Image.open("nagaluv.png"), face_info["facial_area"])
    aligned_target = extract_face(Image.open("oshiluv.png"), target_info["facial_area"])

    perturbed = attack(aligned_img, aligned_target, epsilon=3, alpha=0.3, steps=25)

    full_perturbed = paste_face(
        Image.open("nagaluv.png"), perturbed, face_info["facial_area"]
    )
    Image.fromarray(full_perturbed.astype("uint8")).save("perturbed.png")

    # Verify results
    print("Before attack:", DeepFace.verify("nagaluv.png", "oshiluv.png"))
    print("After attack:", DeepFace.verify("perturbed.png", "oshiluv.png"))

    visualize_results(
        Image.open("nagaluv.png"),
        Image.open("perturbed.png"),
        Image.open("oshiluv.png"),
    )
