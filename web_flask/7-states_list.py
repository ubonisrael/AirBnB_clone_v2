#!/usr/bin/python3
"""starts a flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the connection to the database"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list_page():
    """displays a page containing states"""
    states_list = storage.all(State).values()
    return render_template('7-states_list.html', states=states_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
