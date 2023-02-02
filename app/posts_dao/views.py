from flask import Blueprint, render_template
from app.posts_dao.dao.posts import Posts
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')

posts_ = Posts('data/posts.json')


@posts_blueprint.route('/')
def posts_page():
    posts_.load_posts()
    return render_template("user-feed.html", posts=posts_.posts)

