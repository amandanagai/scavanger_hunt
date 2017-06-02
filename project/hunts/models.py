from project import db, bcrypt
from flask_sqlalchemy import SQLAlchemy

# HuntLocation = db.Table('huntlocation', 
#                     db.Column('id', db.Integer, primary_key=True),
#                     db.Column('hunt_id', db.Integer, db.ForeignKey('hunts.id', ondelete='cascade')),
#                     db.Column('location_id', db.Integer, db.ForeignKey('locations.id', ondelete='cascade')))

class Hunt(db.Model):
    __tablename__ = 'hunts'

    id = db.Column(db.Integer, primary_key=True)
    hunt_name = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'))

    def __init__(self, hunt_name):
        self.hunt_name = hunt_name

    def __repr__(self):
        return "This is the {} hunt".format(self.hunt_name)