from project import db, bcrypt
from flask_sqlalchemy import SQLAlchemy       # Enum, Integer, Text, Column
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    role = db.Column(db.Enum("hunter", "creator", "observer", name="role_type"))
    password = db.Column(db.Text, nullable=False)
    hunts = db.relationship('Hunt', backref='user', lazy='dynamic', cascade='all,delete')

    def __init__(self, username, email, role, password):
        self.username = username
        self.email = email
        self.role = role
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

    def __repr__(self):
        return "User is {}".format(self.username)