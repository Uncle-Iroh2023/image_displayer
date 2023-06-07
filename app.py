import os
import random
from flask import Flask, send_from_directory
from collections import deque

app = Flask(__name__)

last_images = deque(maxlen=10)

@app.route('/')
def display_random_image():
    image_folder = os.path.join(app.root_path, 'images')
    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    if not image_files:
        return "No images found"

    # Filter out the images that have been shown recently
    unseen_images = [img for img in image_files if img not in last_images]

    # If all images have been seen recently, just choose from all images
    if not unseen_images:
        unseen_images = image_files

    random_image = random.choice(unseen_images)

    # Add the shown image to the queue of last shown images
    last_images.append(random_image)

    return send_from_directory(image_folder, random_image)

if __name__ == '__main__':
    app.run(port=8080)
