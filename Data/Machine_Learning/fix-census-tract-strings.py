import csv

reader = csv.reader(open('clean-race-by-census-tract.csv', 'rU'))
writer = csv.writer(open('full-race-by-census-tract.csv', 'w'))
next(reader, None)

for l in reader:
	fips = '{0:03d}'.format(int(l[0]))
	tract = '{0:06d}'.format(int(l[1]))
	writer.writerow([fips+tract] + l[2:])




reader = csv.reader(open('clean-sex-age-by-census-tract.csv', 'rU'))
writer = csv.writer(open('full-sex-age-by-census-tract.csv', 'w'))
next(reader, None)

for l in reader:
	fips = '{0:03d}'.format(int(l[0]))
	tract = '{0:06d}'.format(int(l[1]))
	writer.writerow([fips+tract] + l[2:])