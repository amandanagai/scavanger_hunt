from project import db, bcrypt
from flask_sqlalchemy import SQLAlchemy       # Enum, Integer, Text, Column


class HuntLocation(db.Model):

    __tablename__ = 'huntlocation'

    id = db.Column(db.Integer, primary_key=True)
    hunt_id = db.Column(db.Integer, db.ForeignKey('hunts.id', ondelete='cascade'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id', ondelete='cascade'))
    location_order = db.Column(db.Integer, nullable=False)

    def __init__(self, hunt_id, location_id, location_order):
        self.hunt_id = hunt_id
        self.location_id = location_id
        self.location_order = location_order

    @classmethod
    def highest_order_num(cls, hunt_id):
        highest = cls.query.filter_by(hunt_id=hunt_id).order_by('location_order desc').first()
        if highest is not None:
            return highest.location_order
        return 0

    # @classmethod
    # def max_lat(cls, hunt_id):
    #     locations = cls.query.filter_by(hunt_id=hunt_id).location_id
    #     for location in locations

    #     if highest is not None:
    #         return highest.location_order
    #     return 0



    # @classmethod
    # def delete_and_reorder(cls, id):
    #     to_delete = cls.query.filter_by()

class Location(db.Model):
    
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.Text, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    hunts = db.relationship('Hunt', secondary='huntlocation', backref='locations', lazy='dynamic', cascade='all,delete')


    def __init__(self, place_name, lat, lng):
        self.place_name = place_name
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        return "Location is {}".format(self.place_name)