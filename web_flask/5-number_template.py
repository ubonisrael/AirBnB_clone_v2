#!/usr/bin/python3
"""starts a flask application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns a response for the index route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """returns a response for the hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_dir(text):
    """returns a response for the c dir route"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
def hello_python():
    """returns a response for the python route"""
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def python_dir(text):
    """returns a response for the python dir route"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def num_route(n):
    """returns a response for the number dir route"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:number>", strict_slashes=False)
def num_template_route(number):
    """returns a response for the number_template dir route"""
    return render_template('5-number.html', number=number)


if __name__ == "__main__":
    app.run(debug=True)
