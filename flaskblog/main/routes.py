from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/posts")
def posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=1)
    return render_template("posts.html", title="Posts", posts=posts)
