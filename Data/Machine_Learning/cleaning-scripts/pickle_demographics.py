import csv
import cPickle


def main():
	reader = csv.reader(open('full-race-by-census-tract.csv', 'rU'))
	# csv_writer.writerow(['tract','total','white','black','hispanic','other'])
	demographics = {}
	for r_line in reader:
		tract = census_9_to_census_7(r_line[0])

		if r_line[1] == '0':
			race_weights = [0.0, 0.0, 0.0, 0.0]
		else:
			race_weights = [float(r_line[2]), float(r_line[3]), float(r_line[4]), float(r_line[5])]
		
		race_props = [int(round(p*100.0)) for p in race_weights]
		demographics[tract] = race_props

	import cPickle

	with open('demographics.pkl', 'wb') as fid:
		cPickle.dump(demographics, fid)  
	print demographics

def census_9_to_census_7(tract):
    last_6 = tract[-6:]
    if len(tract) == 8:
        first = '0' + tract[:2]
    elif len(tract) == 9:
        first = tract[:3]

    if first == '047':
        print "BROOKLYN"
        prefix = '3'
    elif first == '061':
        print "MANHATTAN"
        prefix = '1'
    elif first == '005':
        print "THE BRONX"
        prefix = '2'
    elif first == '081':
        print "QUEENS"
        prefix = '4'
    elif first == '085':
        print "STATEN ISLAND"
        prefix = '5'
    else:
        print(tract)

    return prefix + last_6
if __name__ == '__main__':
	main()