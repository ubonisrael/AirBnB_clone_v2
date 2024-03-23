#!/usr/bin/python3
"""starts a flask application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns a response for the index route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """returns a response for the hbnb route"""
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True)
