from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.hunts.models import Hunt
from project.locations.models import Location
# from project.users.models import User
from project.users.views import ensure_correct_user
# from project.locations.forms import LocationForm
from project import db, bcrypt
from functools import wraps
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.exc import IntegrityError


locations_blueprint = Blueprint(
    'locations',
    __name__,
    template_folder='templates'
)

@locations_blueprint.route('/')
def index(user_id, id):
    return render_template('locations/index.html', user_id=user_id, id=id)