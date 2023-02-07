from flask import Flask, request, render_template, send_from_directory
import logging

from app.posts_dao.views import posts_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


@app.errorhandler(500)
def page_not_found(error):
    return render_template('505.html')

#logging.basicConfig(filename="sample.log", filemode='w', level=logging.DEBUG, encoding='utf-8')

app.register_blueprint(posts_blueprint)

app.run(debug=True)