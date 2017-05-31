from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.hunts.models import Hunt
from project.users.models import User
from project.users.views import ensure_correct_user
from project.hunts.forms import HuntForm
from project import db, bcrypt
from functools import wraps
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.exc import IntegrityError


hunts_blueprint = Blueprint(
    'hunts',
    __name__,
    template_folder='templates'
)

@hunts_blueprint.route('/', methods=['GET', 'POST'])
@login_required
# @ensure_correct_user
def index(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        new_hunt = Hunt(request.form['hunt_name'])
        new_hunt.user_id = user.id
        db.session.add(new_hunt)
        db.session.commit()
        return redirect(url_for('hunts.index', user_id=user_id))
    return render_template('hunts/index.html', user=user, hunts=user.hunts)

@hunts_blueprint.route('/new')
@login_required
# @ensure_correct_user
def new(user_id):
    form = HuntForm(request.form)
    return render_template('hunts/new.html', user_id=user_id, form=form)

@hunts_blueprint.route('/<int:id>/edit')
@login_required
# @ensure_correct_user
def edit(user_id, id):
    hunt = Hunt.query.get(id)
    form = HuntForm(obj=hunt)
    return render_template('hunts/edit.html', user_id=user_id, hunt=hunt, form=form)    

@hunts_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@login_required
# @ensure_correct_user
def show(user_id, id):
    hunt = Hunt.query.get(id)
    if request.method == b'PATCH':
        hunt.hunt_name = request.form['hunt_name']
        db.session.add(hunt)
        db.session.commit()
        return redirect(url_for('hunts.index', user_id=user_id))
    if request.method == b'DELETE':

        db.session.delete(hunt)
        db.session.commit()
        return redirect(url_for('hunts.index', user_id=user_id))
    return render_template('hunts/show.html', user_id=user_id, id=id, hunt=hunt)







