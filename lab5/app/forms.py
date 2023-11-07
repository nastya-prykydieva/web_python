from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Username",
                           validators=[
                               DataRequired(message="This field is required.")
                           ])
    password = PasswordField("Password",
                             validators=[
                                 DataRequired(message="This field is required."),
                                 Length(min=4, max=10)
                             ])
    remember = BooleanField("Remember me")
    submit = SubmitField("Log in")
