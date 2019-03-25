from flask_babel import _, get_locale
from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('home.html')