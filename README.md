*Note: This is a WIP. Not finished; was a way to explore the Google Maps API.

Scavanger Hunt

https://scavanger-hunt.herokuapp.com/users/login

Do you like to surprise people with experiences?
Create a fun adventure for a friend or loved ones. Lead her/him/them around a city or location.
You get to decide if there's a surprise waiting for them at the end.

This is a scavanger hunt generating app that allows you to digitally build scavanger hunts for your friends.
It's a work in progress - the eventual goal is to help people run scavenger hunts on the app as well.
Send a pull request if you have ideas or want to help build.


Languages:

Javascript
Python
jQuery
AJAX
SQL
Postgres
HTML
a little CSS (needs more!)


With the following APIs + modules:

Google Maps API
Flask
flask-login
flask-modus
flask-wtf
flask-blueprints
flask-sqlalchemy
flask-migrate
Geocoder
Twitter Bootstrap
bcrypt


To get it up and running locally:

(The following instructions assume a mac environment)
Clone the repo: git clone https://github.com/amandanagai/scavanger_hunt
I recommend making: mkvirtualenv scavenger_hunt
pip install -r requirements.txt
If you don't yet have it, install postgres and then: createdb scavenger_hunt
Database migration/upgrade: python manage.py db upgrade
Start the server: python app.py
Runs on port 5000. http://localhost:5000/


