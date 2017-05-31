from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class HuntForm(FlaskForm):
    hunt_name = StringField('Name your hunt', validators=[DataRequired()])