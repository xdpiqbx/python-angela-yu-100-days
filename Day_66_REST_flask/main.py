import json
import random
from pprint import pprint

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from werkzeug.exceptions import HTTPException

from app_status_messages import *

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self) -> dict[str: int | str | bool]:
        not_allowed_key = '_sa_instance_state'
        return {key: value for key, value in self.__dict__.items() if key != not_allowed_key}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_record():
    total_records = db.session.query(func.count(Cafe.id)).scalar()
    random_offset = random.randint(0, total_records - 1)
    cafe = db.session.query(Cafe).offset(random_offset).first()  # cafe = Cafe.query.offset(random_offset).first()
    return jsonify(cafe.to_dict())


@app.route("/all")
def get_all_cafe():
    all_cafes = db.session.query(Cafe).order_by(Cafe.name)
    return jsonify([cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def get_search_for_cafe():
    loc = request.args.get('loc')
    condition = Cafe.location.like(f"%{loc}%")
    found_cafes = db.session.query(Cafe).where(condition).order_by(Cafe.name)
    cafes = [cafe.to_dict() for cafe in found_cafes]
    return jsonify(cafes=cafes) if cafes else jsonify(error=error_not_found(loc)), 404


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def post_add_new_cafe():
    # db.session.add( # Method if you send form from Postman
    #     Cafe(
    #         name=request.form.get('name'),
    #         map_url=request.form.get('map_url'),
    #         img_url=request.form.get('img_url'),
    #         .....
    #     )
    # )

    data = request.get_json()
    db.session.add(
        Cafe(
            name=data.get('name'),
            map_url=data.get('map_url'),
            img_url=data.get('img_url'),
            location=data.get('location'),
            seats=data.get('seats'),
            has_toilet=data.get('has_toilet'),
            has_wifi=data.get('has_wifi'),
            has_sockets=data.get('has_sockets'),
            can_take_calls=data.get('can_take_calls'),
            coffee_price=f"£{data.get('coffee_price')}"
        )
    )
    db.session.commit()
    return jsonify(response=added_new_cafe())


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def patch_coffe_price(cafe_id):
    data = request.get_json()
    coffee_price = f"£{data.get('coffee_price')}"
    try:
        cafe = db.get_or_404(Cafe, cafe_id)
        cafe.coffee_price = coffee_price
        db.session.commit()
        return jsonify(response=updated_price())
    except HTTPException as error:
        error.description = cafe_not_found_by_id(cafe_id)
        return jsonify(error={error.name: error.description}), error.code


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete_caffe(cafe_id):
    CAFE_KEY = "asighasuldbgsoaudhvsda"
    if dict(request.headers.items()).get('Cafe-Key') != CAFE_KEY:
        return jsonify(error=wrong_api_key()), 403
    try:
        cafe = db.get_or_404(Cafe, cafe_id)
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response=cafe_successfully_removed(cafe.name))
    except HTTPException as error:
        error.description = cafe_not_found_by_id(cafe_id)
        return jsonify(error={error.name: error.description}), error.code


if __name__ == '__main__':
    app.run(debug=True)
