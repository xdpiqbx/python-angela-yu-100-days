from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    email = StringField(
        label='Email',
        validators=[DataRequired()]
    )
    password = PasswordField(
        label='Password',
        validators=[DataRequired()],
    )
    submit = SubmitField(label="Log In")
