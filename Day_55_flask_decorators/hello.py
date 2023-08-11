from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_em(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_u(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/")
@make_bold
@make_em
@make_u
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def bye():
    return "Good bye my friend"


@app.route("/username/<name>")
def greet(name):
    return f"Hello, {name}"


@app.route("/username/<name>/<int:year>")
def years(name, year):
    return f"<p>{name} you are {year} old.</p>"


if __name__ == '__main__':
    app.run(debug=True)
