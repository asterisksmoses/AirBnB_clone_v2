#!/usr/bin/python3

"""After importing the flask module an application instance of
Flask was created."""
from flask import Flask
application = Flask(__name__)

@application.route('/', strict_slashes=False)
def home():
    """This function displays Hello HBNB!"""
    return "Hello HBNB!"

if __name__ == "__main__":
   application.run(host='0.0.0.0', port=5000)
