from app import app
import sqlite3
from flask import g
import cPickle
import csv
from conversion import census_9_to_census_7, format_race

DATABASE = 'stop_and_frisked_graph.db'
DATABASE_1 = 'stop_and_frisked_v01.db'

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

def get_db_1():
    db1 = getattr(g, '_database1', None)
    if db1 is None:
        db1 = g._database = sqlite3.connect(DATABASE_1)
    return db1

@app.teardown_appcontext
def close_connection_1(exception):
    db1 = getattr(g, '_database1', None)
    if db1 is not None:
        db1.close()


def get_demographics():
    with open('web/app/static/data/demographics.pkl', 'rb') as fid:
        return cPickle.load(fid)

def get_income():

    reader = csv.reader(open('web/app/static/data/ACS_13_5YR_B19013_with_ann.csv', 'rU'))
    next(reader)
    next(reader)

    income = {}
    for line in reader:
        tract = census_9_to_census_7(line[1][-9:])
        if tract:
            income[tract] = line[3]

    return income

def get_time_series(requir_dict={}):

    db = get_db()

    if not requir_dict:
        query = "select year,datestop, num from num_graph group by year, datestop"
    else:
        races = convert_races(requir_dict['race'])
        if len(races) > 1:
            raceString = "race in {0}".format(tuple(races))
        else:
            raceString = "race='{0}'".format(races[0])

        query = "select year,datestop,count(datestop) as num from stop_and_frisked where age={0} and sex='{1}' and {2} group by year, datestop".format(requir_dict['age'], requir_dict['sex'], raceString)

    c = db.cursor()
    print '***************', query
    c.execute(query)
    resultset = c.fetchall()

    result_list=[]
    for item in resultset:
        issue_list = ["year", "datestop", "num"]
        if int(item[0]) >= 2006:
            date = item[1] + item[0]
            qty = item[2]
            result_list.append({'date' : date, 'chance' : qty})


    return result_list

def count_total(year, date, age, race, sex):
    db1 = get_db_1()
    c = db1.cursor()

    qualities = ['xcoord', 'ycoord', 'race', 'arstmade']
    races = convert_races(race)

    start_date = date[:2] + "00"
    end_date = date[:2] + "32"
    if len(races) > 1:
        query = "select {0} from stop_and_frisked where year={1} and datestop between '{2}' and '{3}' and age={4} and race in {5} and sex='{6}'"

        query = query.format(','.join(qualities), year, start_date, end_date, age, tuple(races), sex)

    else:
        query = "select {0} from stop_and_frisked where year={1} and datestop between '{2}' and '{3}' and age={4} and race='{5}' and sex='{6}'"
        query = query.format(','.join(qualities), year, start_date, end_date, age, races[0], sex)

        print '***************', query
    c.execute(query)
    resultset = c.fetchall()

    c.close()

    qualities = ['lat', 'lon', 'race', 'arstmade']
    return [dict(zip(qualities, format_item(item))) for item in resultset]


def count_zoom(year,date,minlat,maxlat,minlon,maxlon):
    db1 = get_db_1()
    qualities = ['xcoord', 'ycoord', 'race', 'arstmade']
    c = db1.cursor()

    result_list=[]
    query = "select {0} from stop_and_frisked where year={1} and datestop='{2}' and xcoord between {3} and {4} and ycoord between {5} and {6}"
    query = query.format(','.join(qualities), year, date, minlat, maxlat, maxlon, minlon)
    c.execute(query)
    resultset = c.fetchall()
    c.close()


    #This is hackery b/c they are encoded backwards in the db.
    qualities = ['lat', 'lon', 'race', 'arstmade']
    for item in resultset:
        result_list.append(dict(zip(qualities, format_item(item))))

    return result_list

def convert_races(r):
    races = {'W':['W'],'B':['B'],'H':['P','Q'],'O':['A','I','X','Z']}
    return races[r]

def format_item(item):
    formatted = []
    formatted.append(float(item[0]))
    formatted.append(float(item[1]))
    formatted.append(format_race(item[2]))
    formatted.append(item[3] == 'Y')
    return formatted
