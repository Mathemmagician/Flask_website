import os
from PIL import Image
from flask import url_for, current_app
from werkzeug.utils import secure_filename


def save_post_image(form_image, post_id, image_id):
    _, f_ext = os.path.splitext(form_image.filename)
    image_filename = f"post_{post_id}.image_{image_id}{f_ext}"
    print(image_filename)
    image_path = os.path.join(current_app.root_path, 'static/blog_imgs', image_filename)
    form_image.save(image_path)
    return image_path