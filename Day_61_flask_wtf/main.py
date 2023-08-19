from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request
from login_form import LoginForm

SECRET_KEY = '''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
pipenv install -r ./Day_61_flask_wtf/requirements.txt
'''.encode('utf8')

app = Flask(__name__)
app.secret_key = SECRET_KEY

bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        is_email_correct = form.email.data == 'admin@email.com'
        is_password_correct = form.password.data == '12345678'
        if is_email_correct and is_password_correct:
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template(
        # 'login.html',
        'login_bootstrap_flask.html',
        form=form
    )


if __name__ == '__main__':
    app.run(debug=True)
