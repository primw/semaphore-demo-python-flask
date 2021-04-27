from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SubmitField
from wtforms.validators import DataRequired

class CreateTaskForm(FlaskForm):
    task_title = StringField('Username', validators=[DataRequired()])
    task_description = TextAreaField('Post Contents')
    task_submit = SubmitField('Create Post')