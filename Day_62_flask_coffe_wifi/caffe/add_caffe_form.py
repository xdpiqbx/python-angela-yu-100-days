from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL, Length


class AddCafe(FlaskForm):
    name = StringField(
        label='Cafe Name',
        default=None,
        validators=[
            DataRequired(message="Cafe Name required.")
        ]
    )
    location = StringField(
        label='Google Maps location (url)',
        default=None,
        validators=[
            DataRequired(message="Location required."),
            URL(message="Invalid URL address")
        ]
    )
    open_from = TimeField(
        label='Opening Time',
        default=None,
        validators=[
            DataRequired(message="Open time?")
        ]
    )
    close = TimeField(
        label='Close Time',
        default=None,
        validators=[
            DataRequired(message="Close time?")
        ]
    )
    coffe_rank = SelectField(
        label='Coffe rating',
        choices=['✘', '☕', '☕' * 2, '☕' * 3, '☕' * 4, '☕' * 5],
        validators=[
            DataRequired(message="Set rating"),
            Length(min=1, max=5)
        ]
    )
    wifi_rank = SelectField(
        label='Wifi strength rating',
        choices=['✘', '💪', '💪' * 2, '💪' * 3, '💪' * 4, '💪' * 5],
        validators=[
            DataRequired(message="Set wifi strength rating"),
            Length(min=1, max=5)
        ]
    )
    power = SelectField(
        label='Power socket availability',
        choices=['✘', '🔌', '🔌' * 2, '🔌' * 3, '🔌' * 4, '🔌' * 5],
        validators=[
            DataRequired(message="Set wifi strength rating"),
            Length(min=1, max=5)
        ]
    )

    submit = SubmitField(label="Add Caffe")
