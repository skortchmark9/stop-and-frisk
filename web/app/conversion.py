from pyproj import Proj

#US Survey Feet, NY Long Island
e_3628 = '+proj=lcc +lat_1=41.03333333333333 +lat_2=40.66666666666666 +lat_0=40.16666666666666 +lon_0=-74 +x_0=300000.0000000001 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +to_meter=0.3048006096012192 +no_defs'

p = Proj(e_3628)
to_meter = 0.3048006096012192


def state_2_lat_lng(state_x, state_y):
    state_x = us_ft_2_m(state_x)
    state_y = us_ft_2_m(state_y)
    lng, lat = p(state_x, state_y, inverse=True)
    return lat, lng

def lat_lng_2_state(lat, lng):
    m_x, m_y = p(lng, lat)
    f_x = m_2_us_ft(m_x)
    f_y = m_2_us_ft(m_y)
    return (f_x, f_y)

def us_ft_2_m(ft):
    return ft * to_meter

def m_2_us_ft(m):
    return m / to_meter

def census_9_to_census_7(tract):
    last_6 = tract[-6:]
    if len(tract) == 8:
        first = '0' + tract[:2]
    elif len(tract) == 9:
        first = tract[:3]
    else:
        return None

    if first == '047':
        prefix = '3'
    elif first == '061':

        prefix = '1'
    elif first == '005':

        prefix = '2'
    elif first == '081':
        prefix = '4'
    elif first == '085':
        prefix = '5'
    else:
        return None

    return prefix + last_6
