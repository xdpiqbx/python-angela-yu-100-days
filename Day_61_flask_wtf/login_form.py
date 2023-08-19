from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(
        label='Email',
        default=None,
        validators=[
            DataRequired(message="Email required."),
            Email(message="Invalid Email address")
        ]
    )
    password = PasswordField(
        label='Password',
        validators=[
            DataRequired(message="Email required."),
            Length(min=8, message="Password must be at least 8 characters long")
        ],
    )
    submit = SubmitField(label="Log In")
