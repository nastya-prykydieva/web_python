from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed
from .models import Type


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=100)])
    text = TextAreaField('Text', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(["jpg", "png"])])
    type = SelectField('Type', choices=[e.name for e in Type])
    enabled = BooleanField('Enabled')
    submit = SubmitField('Submit')
