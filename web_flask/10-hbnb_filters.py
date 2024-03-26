#!/usr/bin/python3
"""starts a flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the connection to the database"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Filters through cities and states in DB"""
    states_list = storage.all(State).values()
    amenities_list = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states_list, amenities=amenities_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
