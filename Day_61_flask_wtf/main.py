from flask import Flask, render_template
from login_form import MyForm

SECRET_KEY = '''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
pipenv install -r ./Day_61_flask_wtf/requirements.txt
'''.encode('utf8')

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    form.validate_on_submit()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
