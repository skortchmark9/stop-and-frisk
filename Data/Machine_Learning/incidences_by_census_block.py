import csv
import urllib2
import json

def main():
    get_tract(40.8705486142017, -73.79377266619575)

def get_tract(lat, lon):
    """Looks up tract code given (latitude,longitude) pair"""
    base_url ='http://www.broadbandmap.gov/broadbandmap/census/tract?latitude={0}&longitude={1}&format=json'

    request_url = base_url.format(lat, lon)
    try:
        response = urllib2.urlopen(request_url, timeout=5)
        data = response.read()
        data_dict = json.loads(data)
        return (data_dict['Results']['censusTract'][0]['fips'][-6:])
    except Exception as e:
        print('exception', e)
        pass
    return ("", -1)



if __name__ == '__main__':
    main()
