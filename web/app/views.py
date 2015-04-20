from flask import render_template
from app import app


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/selection')
def index():
    return render_template("selection.html")
