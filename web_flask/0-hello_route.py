#!/usr/bin/python3

from flask import Flask
application = Flask(__name__)
"""After importing the flask module an application instance of
Flask was created."""

@application.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"

if __name__ == "__main__":
   application.run(host='0.0.0.0', port=5000)
