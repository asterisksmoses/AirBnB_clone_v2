#!/usr/bin/python3

"""After importing the flask module an application instance of
Flask was created."""

from flask import Flask
application = Flask(__name__)
application.url_map.strict_slashes = False

@application.route('/', strict_slashes=False)
def home():
    """This function displays Hello HBNB!"""
    return "Hello HBNB!"

@application.route('/hbnb', strict_slashes=False)
def flask_hbnb():
    """This function displays HBNB!"""
    return "HBNB"

@application.route('/c/<text>')
def text_params(text):
    """This function runs the test parts with any parameters."""
     
    text_w_no_underscore = text.replace('_', ' ')
    return "C {}".format(text_w_no_underscore)

@application.route('/python', defaults={'text': 'is_cool'})
@application.route('/python/<text>')
def py_w_text_parameters(text):
    """This function prints the defualt value is_cool."""
    text_w_no_underscore = text.replace('_', ' ')
    return "Python {}".format(text_w_no_underscore)

if __name__ == "__main__":
   application.run(host='0.0.0.0', port=5000)
