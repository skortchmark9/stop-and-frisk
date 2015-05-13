import itertools
import csv
import random as r
import numpy.random as npr


fips_dict = {'BROOKLYN': '047' , 'MANHATTAN': '061', 'BRONX': '005', 'QUEENS': '081', 'STATEN ISLAND': '085', 'STATEN IS': '085'}


for year in range(2008, 2013):
	clean_r = csv.reader(open('clean-'+str(year)+'.csv', 'rU'))
	stop_r = csv.reader(open(str(year)+'-stops.csv', 'rU'))
	next(clean_r, None)

	writer = csv.writer(open('full-'+str(year)+'.csv', 'w'))

	factor = 2

	for c_line, s_line in itertools.izip(clean_r, stop_r):
		if s_line[1] == "('', -1)" or s_line[1] == '':
			continue
		city = c_line[4].strip()
		fips = fips_dict[city]
		tract = '{0:06d}'.format(int(s_line[1]))
		writer.writerow([1, fips+tract] + s_line[2:])