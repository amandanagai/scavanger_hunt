from project import db, bcrypt
from flask_sqlalchemy import SQLAlchemy       # Enum, Integer, Text, Column
from flask_login import UserMixin


class Location(db.Model, UserMixin):
    
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, nullable=False)
    place_name = db.Column(db.Text, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    hunt_id = db.Column(db.Integer, db.ForeignKey('hunts.id', ondelete='cascade'))

    def __init__(self, hunt_name):
        self.order = order
        self.place_name = place_name
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        return "Location #{} is {}".format(self.order, self.place_name)