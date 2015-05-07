from flask import render_template
from app import app
import csv
import json
from conversion import state_2_lat_lng



@app.route('/')
def main():
    return render_template('layout.html', data=getHeatmapSampleData())

@app.route('/selection')
def selection():
    return render_template("selection.html" )

@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html', data=getHeatmapSampleData())


def getHeatmapSampleData():
    sample = open('web/app/static/data/2014_sample.csv')
    reader = csv.DictReader(sample)
    data = []
    for row in reader:
        try:
            state_x = float(row['xcoord'])
            state_y = float(row['ycoord'])
            lat, lng = state_2_lat_lng(state_x, state_y)
            data.append({'lat' : lat, 'lng' : lng, 'race' : row['race']})
        except ValueError as e:
            print('ERROR: ', row['xcoord'], row['ycoord'], row['race'])

    return json.dumps(data)


