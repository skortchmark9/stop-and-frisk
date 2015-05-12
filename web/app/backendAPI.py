from app import app
import sqlite3
from flask import g,Flask,url_for
import cPickle
import csv
from conversion import census_9_to_census_7

DATABASE = 'stop_and_frisked.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

