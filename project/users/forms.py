from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class EditUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])
    current_password = PasswordField('Current password')
    new_password = PasswordField('New password')
    confirm_password = PasswordField('Confirm new password')