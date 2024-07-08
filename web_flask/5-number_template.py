#!/usr/bin/python3
"""
Simple flask app script
App listen on '0.0.0.0'
Port 5000 and defines one route
"""

from flask import Flask
from flask import render_template

# Initialize the flask application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route Handler for the root URL ('/').
    Returns str: Display "Hello HBNB!" on webpage.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Route Handler for the root URL ('/hbnb')
    Returns str: Display "HBNB" on webpage
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    """
    Route handler for the URl pattern '/c/<text>'.
    Replaces underscores in text variable with spaces and
    Returns the string starting with "C :"

    Args:
        text (str): The text to display after "C ".

    Returns:
        str: The string "C " followed by the modified text.
    """
    # Replace underscores with spaces in the text variable
    return 'C ' + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_pythontext(text):
    """
    Route handler for URL pattern '/python/' or '/python/<text>'
    Replaces underscores in the text variable with spaces and
    returns a string with "Python ":

    Args:
        text (str): The text to display after "Python "

    Returns:
        str: The string "Python " followed by the modified text
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """
    Route handler for the URL pattern '/number/<n>'
    Display "n is a number" only if n is an int

    Args:
    n (int): The integer to display

    Returns:
        str: The string "<n> is a number"
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route handler for URL pattern '/number_template/<int:n>'
    Display an HTML page with number only if n is a int
    
    Args:
        n (int): The integer to display.
    
    Returns:
        str: The HTML content with the number.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    # Run Flask app on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
