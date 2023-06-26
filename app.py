#!/var/www/image_displayer/venv/bin/python
import os
import random
from flask import Flask, render_template
from collections import deque

app = Flask(__name__)

last_images = deque(maxlen=10)

@app.route('/', methods=['GET'])
def display_random_image():
    image_folder = os.path.join(app.root_path, 'static/cat')
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

    return render_template("index.html", image=random_image)

if __name__ == '__main__':
    app.run(port=1337,host="0.0.0.0",debug=True)
