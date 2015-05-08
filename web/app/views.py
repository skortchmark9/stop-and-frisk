from flask import render_template, jsonify, request
from app import app
import csv
import json
from conversion import state_2_lat_lng
from collections import Counter
import sys
sys.path.append('/gpfs/main/home/skortchm/course/cs1951-A/stop-and-frisk/web/app/Classifier')
from classify import get_probs_all_tracts

@app.route('/')
def main():
    test_dict = {'time': '01012013', 'sex': 'M', 'race': 'B', 'age': '17'}
    print(get_probs_all_tracts(test_dict))

    data = getSampleData(True, True)
    return render_template('layout.html', heatmap_data=json.dumps(data['heatmap_data']), timeline_graph_data=json.dumps(data['timeline_graph_data']))

@app.route('/selection')
def selection():
    return render_template("selection.html" )

@app.route('/alexa', methods=['POST'])
def alexa():
    print('HIT')
    print(request.form['age'])
    return jsonify(success=True)
    # {'time' : 'MMDDYYYY', 'sex' : 'F/M', 'race' : 'W/H/B/O'. 'age' : '++'}
    # return [{'tract' : 22}]



@app.route('/heatmap')
def heatmap():
    data = getSampleData(True, False)

    return render_template('heatmap.html', heatmap_data=json.dumps(data['heatmap_data']))

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