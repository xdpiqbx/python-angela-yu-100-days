from pprint import pprint

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv
from add_caffe_form import AddCafe

from caffe import Caffe

'''
pipenv install -r ./Day_62_flask_coffe_wifi/requirements.txt
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


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
        data_row = [
            caffe_form.name.data,
            caffe_form.location.data,
            caffe_form.open_from.data.strftime("%#I:%M%p"),
            caffe_form.close.data.strftime("%#I:%M%p"),
            caffe_form.coffe_rank.data,
            caffe_form.wifi_rank.data,
            caffe_form.power.data
        ]
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            csv_file.write('\n')
            csv.writer(csv_file, delimiter=',').writerow(data_row)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=caffe_form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_cafes: list[Caffe] = []
        t_headers = []
        for i, row in enumerate(csv_data):
            if i == 0:
                t_headers = row
                continue
            list_of_cafes.append(Caffe(*row))
    return render_template(
        'cafes.html',
        t_headers=t_headers,
        cafes=list_of_cafes
    )


if __name__ == '__main__':
    app.run(debug=True)
