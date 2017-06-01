from flask import redirect, render_template, request, url_for, Blueprint, flash, jsonify
from project.hunts.models import Hunt
from project.locations.models import Location, HuntLocation
# from project.users.models import User
from project.users.views import ensure_correct_user
# from project.locations.forms import LocationForm
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
    coordArr = []
    if request.method == 'POST':
        lat = request.form['lat']
        lng = request.form['lng']
        place = request.form['place']
        new_place = Location(place, lat, lng)
        db.session.add(new_place)
        db.session.commit()
        highest = HuntLocation.highest_order_num(id)
        hl = HuntLocation(id, new_place.id, highest+1)
        db.session.add(hl)
        db.session.commit()
        list_to_pass = [lat, lng, place, hl.location_order]
        return jsonify(list_to_pass)
    return render_template('locations/index.html', user_id=user_id, id=id, coord=coordArr)

# @locations_blueprint.route('/<int:id>/show', methods=['DELETE'])
# def show(user_id, id, ):

@locations_blueprint.route('/geocode', methods=['POST'])
def geocode(user_id, id):
    coord_list = geocoder.google(request.form['place']).latlng
    place = request.form['place']
    coord_list.append(place)
    return jsonify(coord_list)
