#!/usr/bin/python3

from flask import Flask
application = Flask(__name__)
"""After importing the flask module an application instance of
Flask was created."""

@application.route('/', strict_slashes=False)
def home():
    """This function displays Hello HBNB!"""
    return "Hello HBNB!"

@application.route('/hbnb', strict_slashes=False)
def flask_hbnb():
    """This function displays HBNB!"""
    return "HBNB"

if __name__ == "__main__":
   application.run(host='0.0.0.0', port=5000)
