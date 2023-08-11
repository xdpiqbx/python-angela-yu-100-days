# export FLASK_APP=./Day_56_flask_html_static/personal-site/app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
