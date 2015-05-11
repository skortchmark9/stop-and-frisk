from app import app
import sqlite3
from flask import g

DATABASE = 'stop_and_frisked_graph.db'

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

def get_demographics():
    with open('web/app/static/data/demographics.pkl', 'rb') as fid:
        return cPickle.load(fid)


def get_time_series(requir_dict=[]):
    db1 = get_db()
    #table num_graph
    #create table num_graph as select year,datestop,count(year) as num from stop_and_frisked group by year,datestop
    query = "select year,datestop,count(year) as num from stop_and_frisked where "
    query1 = "select * from num_graph"
    value_list=[]

    if len(requir_dict)>0:
        for key in requir_dict:
            query += key + "=? and "
            value_list.append(requir_dict[key])
        values = tuple(value_list)
        query = query.strip(" and ")
        query += " group by year,datestop"
        c = db1.cursor()
        c.execute(query, values)
        resultset = c.fetchall()
        c.close()
    else:
        c = db1.cursor()
        c.execute(query1)
        resultset=c.fetchall()
        c.close()

    result_list=[]
    for item in resultset:
        issue_list =["year", "datestop", "num"]
        date = item[1] + item[0]
        qty = item[2]
        result_list.append({'date' : date, 'chance' : qty})

    return result_list
