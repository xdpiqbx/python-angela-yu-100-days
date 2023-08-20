from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from caffe.add_caffe_form import AddCafe
from db.database import Database, CSVDatabase

'''
pipenv install -r ./Day_62_flask_coffe_wifi/requirements.txt
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

db: Database = CSVDatabase()


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    caffe_form = AddCafe()
    if caffe_form.validate_on_submit():
        db.save_data(caffe_form)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=caffe_form)


@app.route('/cafes')
def cafes():
    data = db.get_data()
    return render_template(
        'cafes.html',
        t_headers=data.get("t_headers"),
        cafes=data.get("list_of_cafes")
    )


if __name__ == '__main__':
    app.run(debug=True)
