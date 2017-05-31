from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.users.models import User
from project import db,bcrypt
from functools import wraps
from project.users.forms import UserForm, LoginForm, EditUserForm
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.exc import IntegrityError


users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)


def ensure_correct_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('id') != current_user.id:
            flash("Not Authorized")
            return redirect(url_for('hunts.index', user_id=current_user.id))
        return fn(*args, **kwargs)
    return wrapper

@users_blueprint.route('/')
def index():
    return redirect(url_for('users.login'))

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserForm(request.form)
    if form.validate_on_submit():                   # vs. .validate(), .validate_on_submit() checks post/patch/delete + validate
        try:
            new_user = User(form.data['username'], form.data['email'], form.data['role'], form.data['password'])
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError as e:                 # without this block, the server would crash when the db complained
            flash('Username already taken')
            return render_template('signup.html', form=form)
        flash('User created, please login to continue')
        return redirect(url_for('users.login'))
    return render_template('users/signup.html', form=form)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.data['username']).first()
        if user and bcrypt.check_password_hash(user.password, form.data['password']):
            flash('You have successfully logged in!')
            login_user(user)
            return redirect(url_for('hunts.index', user_id=user.id))
        flash('Invalid credentials')
    return render_template('users/login.html', form=form)

@users_blueprint.route('/<int:id>/edit')
@login_required
def edit(id):
    user = User.query.get(id)
    form = EditUserForm(obj=user)
    form = UserForm(obj=user)
    return render_template('users/edit.html', user=user, form=form)

@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@login_required
@ensure_correct_user
def show(id):
    user = User.query.get(id)
    if request.method == b'PATCH':
        form = EditUserForm(request.form)
        user.username = request.form['username']
        user.email = request.form['email']
        user.role = request.form['role']
        if request.form['current_password'] and bcrypt.check_password_hash(user.password, request.form['current_password']):
            if request.form['new_password'] == request.form['confirm_password']:
                user.password = bcrypt.generate_password_hash(request.form['new_password']).decode('UTF-8') 
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('hunts.index'))
            flash('Invalid credentials.')
            return redirect(url_for('users.edit', id=id))
    if request.method == b'DELETE':
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('users.signup'))
    return render_template('users/show.html', user=user)

@users_blueprint.route('/logout')
@login_required
def logout():
    flash("You're now logged out. Sign back in to visit us again :)")
    logout_user()
    return redirect(url_for('users.login'))






# @users_blueprint.route('/new')
# def new():
#     form = UserForm(request.form)
#     return render_template('/new.html', form=form)


# @users_blueprint.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         form = UserForm(request.form)
#         new_user = UserForm(request.form['username'], request.form['email']. request.form['role'], request.form['password'])
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect(url_for('users.index'))
#     return render_template('index.html', users=User.query.all())
