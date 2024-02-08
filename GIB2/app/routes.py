"""This file will store the different web adresses you have, and works as a directory too look up the different parts
 of the application. This calls the @app.route function in flask, and checks for the input navigation keyword. Remember
 that if you dont place any redirection to a HTML file, the HTML file will not rendered*

 *There are ways of linking HTML files directly in text on other HTML files, but this is not recomended practice in
 flask. If you rather want to use flask as an API, you would define endpoints serving information instead of HTML pages.  """

from flask import render_template
from app import app


@app.route('/')
#@app.route('/index')
def index():
    return "Hello, World!"



