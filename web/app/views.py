from flask import render_template
from app import app
import csv
from pyproj import Proj

#US Survey Feet, NY Long Island
e_3628 = '+proj=lcc +lat_1=41.03333333333333 +lat_2=40.66666666666666 +lat_0=40.16666666666666 +lon_0=-74 +x_0=300000.0000000001 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +to_meter=0.3048006096012192 +no_defs'

p = Proj(e_3628)
to_meter = 0.3048006096012192


@app.route('/')
def main():
    return render_template('pages.html')

@app.route('/selection')
def selection():
    return render_template("selection.html" )

@app.route('/heatmap')
def heatmap():
    sample = open('Data/2014_sample.csv')
    reader = csv.DictReader(sample)
    for row in reader:
        state_x = float(row['xcoord'])
        state_y = float(row['ycoord'])
        lat, lng = state_2_lat_lng(state_x, state_y)
        print(lat, lng, row['race'])
        break

    return render_template('heatmap.html')

def state_2_lat_lng(state_x, state_y):
    state_x = state_x * to_meter
    state_y = state_y * to_meter
    lng, lat = p(state_x, state_y, inverse=True)
    return lat, lng

def lat_lng_2_state(lat, lng):
    m_x, m_y = p(lng, lat)
    m_x = m_x / to_meter
    m_y = m_y / to_meter
    return (m_x, m_y)

def us_ft_2_m(ft):
    return ft * to_meter

def m_2_us_ft(m):
    return m / to_meter

