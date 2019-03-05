from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
class AddTaskForm(Form):
    title=StringField('Title', validators=[DataRequired("Please enter the title.")])
    description=StringField('Description', validators=[DataRequired("Please enter the description.")])
    done=StringField('Done: True/False', validators=[DataRequired("Please enter if it is done")])
    submit=SubmitField('Submit')
