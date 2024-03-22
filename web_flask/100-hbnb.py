#!/usr/bin/python3
"""starts a flask application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def teardown_db(exception):
    """closes the connection to the database"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Filters through cities and states in DB"""
    states_list = []
    amenities_list = []
    places_list = []
    users_list = []
    for item in storage.all("State").values():
        states_list.append(item)
    for item in storage.all("Amenity").values():
        amenities_list.append(item)
    for item in storage.all("Place").values():
        places_list.append(item)
    for item in storage.all("User").values():
        users_list.append(item)
        print(item.id)
    return render_template('100-hbnb.html',
                           states=states_list, amenities=amenities_list,
                           places=places_list, users=users_list)
