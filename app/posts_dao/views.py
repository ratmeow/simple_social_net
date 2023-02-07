from flask import Blueprint, render_template, request

from app.posts_dao.dao.posts import Posts
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')

posts_ = Posts('data/posts.json')


@posts_blueprint.route('/')
def posts_page():
    posts_.load_posts()
    return render_template("index.html", posts=posts_.posts)


@posts_blueprint.route('/posts/<int:postid>')
def post_view(postid):
    posts_.load_posts()
    post = posts_.get_post_by_id(postid)
    return render_template("post.html", post=post)


@posts_blueprint.route('/search')
def post_search():
    s = request.args['s']
    posts_.load_posts()
    posts = posts_.get_posts_by_keyword(s)
    return render_template("search.html", posts=posts)


@posts_blueprint.route('/users/<username>')
def post_search_name(username):
    posts_.load_posts()
    posts = posts_.get_post_by_name(username)
    return render_template("user-feed.html", posts=posts)


@posts_blueprint.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

