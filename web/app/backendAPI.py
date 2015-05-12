from app import app
import sqlite3
from flask import g,Flask,url_for
from conversion import state_2_lat_lng

DATABASE = 'stop_and_frisked_v01.db'

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


def count_zoom(year,date,minlat,maxlat,minlon,maxlon):
	db1 = get_db()
	query = "select xcoord,ycoord,race from stop_and_frisked where year=? and datestop=? and xcoord between ? and ? and ycoord between ? and ?"
	c = db1.cursor()
	value_list=[year,date,minlon,maxlon,minlat,maxlat]
	values = tuple(value_list)
	
	result_list=[]
	c.execute(query, values)
	resultset = c.fetchall()
	c.close()

    for item in resultset:
    	lng = item[13]
    	lat = item[14]
    	race = item[8]
    	result_list.append({'lng' : lng, 'lat' : lat, 'race':race})

    return result_list