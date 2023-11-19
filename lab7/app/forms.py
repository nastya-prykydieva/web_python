from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=14)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=7)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old password", validators=[DataRequired(), Length(min=4, max=10)])
    new_password = PasswordField("New password", validators=[DataRequired(), Length(min=4, max=10)])
    confirm_password = PasswordField("Confirm new password", validators=[DataRequired(), Length(min=4, max=10)])
    submit = SubmitField("Submit")


class ToDoForm(FlaskForm):
    todo = StringField("Enter a task here", validators=[DataRequired(), Length(min=1, max=50)])
    description = StringField("Enter a description here", validators=[DataRequired(), Length(min=1, max=255)])
    submit = SubmitField("Save")


class FeedbackForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired(), Length(min=4, max=14)])
    text = StringField("Leave your feedback here", validators=[DataRequired()])
    submit = SubmitField("Submit")
