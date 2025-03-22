# blog/view.py
from flask import jsonify, Blueprint

# Create a Blueprint for the blog app
bp_blog = Blueprint('blog', __name__)

@bp_blog.route('/blog/post')
def blog_post():
    return jsonify({"message": "This is a blog post!"})

@bp_blog.route('/blog/comment')
def blog_comment():
    return jsonify({"message": "This is a blog comment!"})