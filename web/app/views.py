from flask import render_template, jsonify, request
from app import app
import csv
import json
from conversion import state_2_lat_lng
from collections import Counter
import sys
from classify import get_probs_all_tracts
from db import get_time_series


@app.route('/')
def main():
    total = json.dumps(get_time_series({}))

    return render_template('layout.html', timeline_data=total)

@app.route('/selection')
def selection():
    return render_template("selection.html" )

@app.route('/update_heatmap', methods=['POST'])
def update_heatmap():
    d = {k : v for k, v in request.form.iteritems()}
    d2 = d.copy()
    del d2['time']
    specific = get_time_series(d2)
    probs = get_probs_all_tracts(d)
    return jsonify(success=True, results=probs, time_series=specific)

@app.route('/sf_heatmap')
def sf_heatmap():
    test_dict = {'time': '01012013', 'sex': 'M', 'race': 'O', 'age': '21'}
    tracts = get_probs_all_tracts(test_dict)

    return render_template('sf_heatmap.html', sf_data=tracts)

@app.route('/help')
def help():
    data = []
    for year in range(2006, 2015):
        csv_reader = csv.reader(open(('stop-data/clean-' + str(year) +'.csv'), 'rU'))
        next(csv_reader, None)
        for line in csv_reader:
            lat, lon = state_2_lat_lng(int(line[5]), int(line[6]))
            if lat == '':
                continue
            data.append((lat, lon))
    return render_template('census_block_finder.html', heatmap_data=data)

def getSampleData(heatmap=False, timeline_graph_data=False):
    sample = open('web/app/static/data/2014_sample.csv')
    reader = csv.DictReader(sample)
    heatmap_data = []
    timeline_counter = Counter()

    for row in reader:
        try:
            if heatmap:
                state_x = float(row['xcoord'])
                state_y = float(row['ycoord'])
                lat, lng = state_2_lat_lng(state_x, state_y)
                heatmap_data.append({'lat' : lat, 'lng' : lng, 'race' : row['race']})

            if timeline_graph_data:
                datestop = row['datestop']
                if len(datestop) == 7:
                    datestop = '0' + datestop

                timeline_counter[datestop] += 1

        except ValueError as e:
            print('ERROR: ', row['xcoord'], row['ycoord'], row['race'])

    total = sum([timeline_counter[k] for k in timeline_counter])
    timeline_data = [{'date' : k, 'chance' : int(v * 100/ total)} for k, v in timeline_counter.iteritems()]

    data = {'heatmap_data' : heatmap_data, 'timeline_graph_data' : timeline_data}

    return data
