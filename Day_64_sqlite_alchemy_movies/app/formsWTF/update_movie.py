from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, HiddenField
from wtforms.validators import DataRequired, Length, NumberRange


class UpdateMovieForm(FlaskForm):
    rating = FloatField(
        label='Rating from 0.1 to 10.0',
        validators=[
            DataRequired(message="Rating required."),
            NumberRange(min=0, max=10.0, message="Must be from 0 to 10.0")
        ]
    )
    review = StringField(
        label='Review',
        validators=[
            DataRequired(message="Review required."),
            Length(min=10, max=500, message="Minimum 10 symbols, Max - 500.")
        ]
    )
    movie_id = HiddenField()
    submit = SubmitField(label="Update")
