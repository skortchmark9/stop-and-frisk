import sys
import csv
import collections as c


def main():
	args = sys.argv
	if len(args) != 3:
		print 'Useage: clean-stop-and-frisk.py <data filename>\
		 <output filename>'
		return
	csv_reader = csv.reader(open(args[1], 'rU'))
	csv_writer = csv.writer(open(args[2], 'w'))
	next(csv_reader, None) # skip header

	# 12 years
	# 12 months
	# 2 genders 
	# 85 ages - 19 buckets
	# 9 races
	# 5 cities 

	buckets = c.defaultdict(int)

	for line in csv_reader:
		attributes = line
		date = line[0]
		attributes[0] = date[:(len(date)-6)]
		buckets[tuple(attributes)] += 1

	print len(buckets)

	for key, value in buckets.iteritems():
		print value

if __name__ == '__main__':
	main()