from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
bcrypt = Bcrypt(app)
modus = Modus(app)

if os.environ.get('ENV') == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'change this secret key'
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.hunts.views import hunts_blueprint
from project.locations.views import locations_blueprint
from project.users.models import User
from project.hunts.models import Hunt
from project.locations.models import Location

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(hunts_blueprint, url_prefix='/users/<int:user_id>/hunts')
app.register_blueprint(locations_blueprint, url_prefix='/users/<int:user_id>/hunts/<int:id>/locations')

login_manager.login_view = "users.login"
login_manager.login_message = "Please log in!"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) 


@app.route('/')
def root():
    return redirect(url_for('users.login'))

    # https://scavanger-hunt.herokuapp.com/users/login
    # h3lpH#LP