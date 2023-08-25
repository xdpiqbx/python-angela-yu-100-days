from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class AddMovieForm(FlaskForm):
    title = StringField(
        label='Input movie title',
        validators=[
            DataRequired(message="Field required."),
            Length(min=1, max=250, message="Minimum 1 symbols, Max - 250.")
        ]
    )
    submit = SubmitField(label="Add Movie")
