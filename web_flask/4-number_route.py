#!/usr/bin/python3
"""
Flask web application that listens on 0.0.0.0, port 5000.
Provides several routes:
1. /: displays “Hello HBNB!”
2. /hbnb: displays “HBNB”
3. /c/<text>: displays “C ” followed by the value of the text variable
   (replaces underscore _ symbols with a space)
4. /python/(<text>): displays “Python ” followed by the value of the text variable
   (replaces underscore _ symbols with a space). The default value of text is “is cool”.
5. /number/<n>: displays “n is a number” only if n is an integer.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' for the root route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' for the /hbnb route.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays 'C ' followed by the value of the text variable.
    Replaces underscore _ symbols with a space.
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays 'Python ' followed by the value of the text variable.
    Replaces underscore _ symbols with a space.
    The default value of text is 'is cool'.
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays 'n is a number' only if n is an integer.
    """
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
