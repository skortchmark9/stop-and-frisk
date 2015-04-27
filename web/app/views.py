from flask import render_template
from app import app

@app.route('/')
def main():
    return render_template('pages.html')

@app.route('/selection')
def selection():
    return render_template("selection.html" )

@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html')
