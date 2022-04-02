import json
import uuid
from datetime import datetime

from flask import Flask, g
from flask import request
from flask import render_template

from model.post import Post
from model.user import User
from errors import register_error_handlers

from security.basic_authentication import generate_password_hash
from security.basic_authentication import init_basic_auth


app = Flask(__name__)
auth = init_basic_auth()
register_error_handlers(app)


@app.route("/api/posts", methods = ["POST"])
@auth.login_required
def create_post():
    post_data = request.get_json(force=True, silent=True)
    if post_data is None:
        return "Bad request", 400

    username = auth.username
    user = User.find_by_username(username)
    post = Post(
        title=post_data["title"],
        content=post_data["content"],
        price=post_data["price"],
        is_active=1,  # The field is_active is set to 1 when new ad is created
        buyer=None,  # The field buyer is set to None when new ad is created
        user_id=user.id,  # The owner of the post
        publication_date=datetime.datetime.now()
                )
    post.save()
    return json.dumps(post.to_dict()), 201


@app.route("/api/posts", methods = ["GET"])
def list_posts():
    result = {"result": []}
    for post in Post.all():
        result["result"].append(post.to_dict())
    return json.dumps(result)


@app.route("/api/posts/<post_id>", methods = ["GET"])
def get_post(post_id):
    return json.dumps(Post.find(post_id).to_dict())


@app.route("/api/posts/<post_id>", methods = ["DELETE"])
def delete_post(post_id):
    Post.delete(post_id)
    return ""


@app.route("/api/posts/<post_id>", methods = ["PATCH"])
def update_post(post_id):
    post_data = request.get_json(force=True, silent=True)
    if post_data is None:
        return "Bad request", 400

    post = Post.find(post_id)
    if "title" in post_data:
        post.title = post_data["title"]
    if "content" in post_data:
        post.content = post_data["content"]
    return json.dumps(post.save().to_dict())


@app.route("/api/users", methods = ["POST"])
def create_user():
    user_data = request.get_json(force=True, silent=True)
    if user_data is None:
        return "Bad request", 400
    hashed_password = generate_password_hash(user_data["password"])
    user = User(
        username=user_data["username"],
        password=hashed_password,
        email=user_data["email"],
        address=user_data["address"],
        phone=user_data["phone"]
    )
    user.save()
    return json.dumps(user.to_dict()), 201


@app.route("/", methods = ["GET"])
@auth.login_required
def posts():
    return render_template("index.html")


@app.route("/posts/<post_id>", methods = ["GET"])
def view_post(post_id):
    return render_template("post.html", post=Post.find(post_id))


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
