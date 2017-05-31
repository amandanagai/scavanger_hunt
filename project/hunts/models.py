from project import db, bcrypt
from flask_sqlalchemy import SQLAlchemy       # Enum, Integer, Text, Column
from flask_login import UserMixin


class Hunt(db.Model, UserMixin):
    __tablename__ = 'hunts'

    id = db.Column(db.Integer, primary_key=True)
    hunt_name = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'))
    locations = db.relationship('Location', backref='hunt', lazy='dynamic', cascade='all,delete')

    def __init__(self, hunt_name):
        self.hunt_name = hunt_name

    def __repr__(self):
        return "This is the {} hunt".format(self.hunt_name)