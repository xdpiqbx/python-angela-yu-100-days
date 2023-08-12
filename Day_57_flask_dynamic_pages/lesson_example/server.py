# export FLASK_APP=./Day_57*/server.py
import random
from datetime import datetime
from pprint import pprint

from requests import get
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template(
        'index.html',
        num=random_number,
        year=f"{datetime.now().year}"
    )


@app.route("/guess/<string:name>")
def guess(name: str):  # <a href="{{ url_for('guess', name='Angela') }}">Guess</a>
    age_res = get(f"https://api.agify.io/?name={name}").json()
    gender_res = get(f"https://api.genderize.io/?name={name}").json()
    return render_template(
        'guess.html',
        name=name.title(),
        gender=gender_res.get('gender'),
        age=age_res.get('age')
    )


@app.route("/blog")
@app.route("/blog/<int:num>")
def get_blog(num=None):  # <a href="{{ url_for('get_blog') }}">Blog</a>
    posts = get("https://api.npoint.io/c790b4d5cab58020d391").json()
    pprint(posts)
    return render_template(
        'blog.html',
        posts=posts,
        num=num
    )


if __name__ == '__main__':
    app.run(debug=True, port=5001)
