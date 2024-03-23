#!/usr/bin/python3
"""starts a flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the connection to the database"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Filters through cities and states in DB"""
    states_list = storage.all(State).values()
    amenities_list = storage.all(Amenity).values()
    places_list = storage.all(Place).values()
    users_list = storage.all(User).values()
    return render_template('100-hbnb.html',
                           states=states_list, amenities=amenities_list,
                           places=places_list, users=users_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
