import os
import random
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def display_random_image():
    image_folder = os.path.join(app.root_path, 'images')
    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    if not image_files:
        return "No images found"
    random_image = random.choice(image_files)
    return send_from_directory(image_folder, random_image)

if __name__ == '__main__':
    app.run(port=8080)