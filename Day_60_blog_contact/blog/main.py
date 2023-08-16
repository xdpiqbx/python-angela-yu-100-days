from pprint import pprint

from flask import Flask, render_template, redirect
from post import Post
from flask import request
from notification_manager import NotificationManager

app = Flask(__name__)

@app.context_processor
def inject_header_data():
    header_data = {
            "title": "Blog",
            "subtitle": "My Blog, My rules",
            "bg_image_url": "/static/assets/img/home-bg.jpg"
        }
    if 'header_data' in globals():
        header_data.update(header_data)
    return dict(header_data=header_data)

@app.route('/')
def home():
    return render_template(
        "index.html",
        posts=post_obj.get_posts(),
        title="Blog | Home",
        header_data={
            "title": "Blog",
            "subtitle": "Home page",
            "bg_image_url": "/static/assets/img/home-bg.jpg"
        }
    )

@app.route('/about')
def about():
    return render_template(
        "about.html",
        title="Blog | About",
        header_data={
            "title": "About Me",
            "subtitle": "This is what i do",
            "bg_image_url": "/static/assets/img/about-bg.jpg"
        }
    )

@app.route('/post/<int:post_id>')
def post(post_id: int = 1):
    post_item = post_obj.get_post_by_id(post_id)
    if not post_item:
        return redirect('/')
    return render_template(
        "post.html",
        post=post_item,
        title="Blog | Post",
        header_data={
            "title": post_item.get('title'),
            "subtitle": post_item.get('subtitle'),
            "bg_image_url": "/static/assets/img/post-bg.jpg"
        }
    )

@app.route('/contact')
def contact():
    return render_template(
        "contact.html",
        title="Blog | Contact",
        form_action="send_message",
        header_data={
            "title": "Contact Me",
            "subtitle": "Have questions? I have answers",
            "bg_image_url": "/static/assets/img/contact-bg.jpg"
        }
    )

@app.route('/send_message', methods=['POST'])
def send_message():
    # Here normally validate data.
    data = {
        "name": request.form['name'],
        "email": request.form['email'],
        "phone": request.form['phone'],
        "message": request.form['message'],
    }
    nm = NotificationManager(data)
    nm.send_email()
    return render_template(
        "message_submitted.html",
        title="Blog | Successfully send",
        name=data.get("name"),
        header_data={
            "title": "Successfully send your message",
            "subtitle": "Have a good day =)",
            "bg_image_url": "/static/assets/img/contact-bg.jpg"
        }
    )


if __name__ == "__main__":
    post_obj = Post()
    app.run(debug=True)
