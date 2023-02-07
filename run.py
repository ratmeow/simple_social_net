from flask import Flask, request, render_template, send_from_directory
import logging

from app.posts_dao.views import posts_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

#logging.basicConfig(filename="sample.log", filemode='w', level=logging.DEBUG, encoding='utf-8')

app.register_blueprint(posts_blueprint)

app.run(debug=True)