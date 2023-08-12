from flask import Flask, render_template, redirect
from post import Post


app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        "index.html",
        posts=post_obj.get_posts()
    )

@app.route('/<int:post_id>')
def post(post_id):
    post_item = post_obj.get_post_by_id(post_id)
    if not post_item:
        return redirect('/')
    return render_template(
        "post.html",
        post=post_item
    )

if __name__ == "__main__":
    post_obj = Post()
    app.run(debug=True)
