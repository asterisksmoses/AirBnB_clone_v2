#!/usr/bin/python3

"""After importing the flask module an application instance of
Flask was created."""

from flask import Flask, render_template
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

@application.route('/number/<int:n>')
def fl_number(n):
    """This function ensures that a number is passed as a
parameter."""
    return "{} is a number".format(n)

@application.route('/number_template/<int:n>')
def num_template(n):
    """This function prints a number template."""
    return render_template('5-number.html', num=n)

@application.route('/number_odd_or_even/<int:n>')
def num_odd_or_ev(n):
    """This function checks if a number is odd or even."""
    odd_or_ev = "even" if n % 2 == 0 else "odd"
    elements = {
        "num" : n,
        "odd_or_ev": odd_or_ev
}
    return render_template('6-number_odd_or_even.html', elements=elements)


if __name__ == "__main__":
   application.run(host='0.0.0.0', port=5000)
