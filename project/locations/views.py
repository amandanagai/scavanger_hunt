from flask import redirect, render_template, request, url_for, Blueprint, flash, jsonify
from project.hunts.models import Hunt
from project.locations.models import Location, HuntLocation
# from project.users.models import User
from project.users.views import ensure_correct_user
from project import db, bcrypt
from functools import wraps
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.exc import IntegrityError
import geocoder


locations_blueprint = Blueprint(
    'locations',
    __name__,
    template_folder='templates'
)

@locations_blueprint.route('/', methods=['GET', 'POST'])
def index(user_id, id):
    if "X-Requested-With" in request.headers:
        if request.method == 'POST':
            lat = request.form['lat']
            lng = request.form['lng']
            place = request.form['place']
            hint = request.form['hint']
            new_place = Location(place, lat, lng)
            db.session.add(new_place)
            db.session.commit()
            highest = HuntLocation.highest_order_num(id)
            hl = HuntLocation(id, new_place.id, highest+1, hint)
            db.session.add(hl)
            db.session.commit()
            list_to_pass = [lat, lng, place, hl.location_order, hint]
            return jsonify(list_to_pass)
        if request.method == 'GET':
            markers_dets = []
            hunt = Hunt.query.get(id)
            markers = hunt.locations
            for mark in markers:
                hunt_location = HuntLocation.query.filter_by(location_id=mark.id).filter_by(hunt_id=id).first()
                mark_dets = [mark.lat, mark.lng, hunt_location.location_order, hunt_location.id]
                markers_dets.append(mark_dets)
            return jsonify(markers_dets)
    return render_template('locations/index.html', user_id=user_id, id=id)

@locations_blueprint.route('/geocode', methods=['POST'])
def geocode(user_id, id):
    coord_list = geocoder.google(request.form['place']).latlng
    place = request.form['place']
    coord_list.append(place)
    return jsonify(coord_list)

@locations_blueprint.route('/delete', methods=['DELETE'])
def delete(user_id, id):
    to_delete = HuntLocation.query.get(request.form['huntLocationId'])
    db.session.delete(to_delete)
    db.session.commit()
    return jsonify({})