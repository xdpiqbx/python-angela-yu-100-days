from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        "index.html",
        title="Home Page",
        form_action="login"
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template(
            "login.html",
            title="Login",
            credentials={
                "username": request.form['username'],
                "password": request.form['password']
            }
        )
    else:
        return "GET"

if __name__ == "__main__":
    app.run(debug=True)
