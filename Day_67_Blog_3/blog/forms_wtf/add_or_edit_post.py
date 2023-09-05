from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL
from flask_ckeditor import CKEditorField


def validate_url_or_none(form, field):
    if not field.data.strip():
        return None
    return URL(require_tld=True, message="It must be valid URL address")(form, field)


class AddEditPost(FlaskForm):
    title = StringField(
        label='Title',
        validators=[
            DataRequired(message="Field required."),
            Length(min=1, max=250, message="Minimum 1 symbols, Max - 250.")
        ]
    )
    subtitle = StringField(
        label='Subtitle',
        validators=[
            DataRequired(message="Field required."),
            Length(min=1, max=250, message="Minimum 1 symbols, Max - 250.")
        ]
    )
    author = StringField(
        label='Author name',
        validators=[
            DataRequired(message="Field required."),
            Length(min=1, max=250, message="Minimum 1 symbols, Max - 250.")
        ]
    )
    url_bg_img = StringField(
        label='URL to background image',
        validators=[
            validate_url_or_none
        ]
    )
    content = CKEditorField(
        label='Post content',
        validators=[
            DataRequired(message="Field required."),
            Length(min=10, max=5000)
        ]
    )
    submit = SubmitField(label="Add post")
