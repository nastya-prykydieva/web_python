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


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old password",
                                 validators=[
                                     DataRequired(),
                                     Length(min=4, max=10)
                                 ])
    new_password = PasswordField("New password",
                                 validators=[
                                     DataRequired(),
                                     Length(min=4, max=10)
                                 ])
    confirm_password = PasswordField("Confirm new password",
                                     validators=[
                                         DataRequired(),
                                         Length(min=4, max=10)
                                     ])
    submit = SubmitField("Submit")


class ToDoForm(FlaskForm):
    todo = StringField("Enter a task here",
                       validators=[
                           DataRequired(),
                           Length(min=1, max=50)
                       ])
    description = StringField("Enter a description here",
                              validators=[
                                  DataRequired(),
                                  Length(min=1, max=255)
                              ])
    submit = SubmitField("Save")
