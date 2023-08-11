import random
from flask import Flask

app = Flask(__name__)

HOME_PAGE_IMAGE = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'
FOUND_IMAGE = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'
TO_HIGH_IMAGE = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
TO_LOW_IMAGE = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'

def add_image(src_arg):
    def decorator(function):
        def wrapper():
            return (f"{function()}"
                    f"<img src='{src_arg}'/>")
        return wrapper
    return decorator

@add_image(HOME_PAGE_IMAGE)
def home_message():
    return "<h1>Guess a number between 0 and 9</h1>"

@add_image(FOUND_IMAGE)
def found_message():
    return "<h1>You found me!</h1>"

@add_image(TO_HIGH_IMAGE)
def high_message():
    return "<h1>Too high, try again!</h1>"

@add_image(TO_LOW_IMAGE)
def low_message():
    return "<h1>Too low, try again!</h1>"

@app.route("/")
def home():
    return home_message()

def you_found_me_and_get_new_rand():
    global rand_number
    rand_number = random.choice(range(0, 10))
    print(rand_number)
    return found_message()

@app.route("/<int:number>")
def try_guess(number):
    if number == rand_number:
        return you_found_me_and_get_new_rand()
    return low_message() if number < rand_number else high_message()

if __name__ == '__main__':
    rand_number = random.choice(range(0, 10))
    print(rand_number)
    app.run(debug=True)
