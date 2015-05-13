import itertools
import csv
import sys
from conversion import state_2_lat_lng
from incidences_by_census_block import get_tract
import random as r
import numpy.random as npr
import thread


def main():
 	format_file(int(sys.argv[1]))

def format_file(year):
	csv_reader = csv.reader(open(('stop-data/clean-' + str(year) +'.csv'), 'rU'))
	csv_writer = csv.writer(open(str(year) + '-stops.csv', 'w'))
	next(csv_reader, None)
	for line in csv_reader:
		lat, lon = state_2_lat_lng(int(line[5]), int(line[6]))
		if lat == '':
			continu
		tract = get_tract(lat, lon)
		time = str_to_time(line[0])
		sex = line[1]
		race = format_race(line[2])
		age =  (int(line[3]) - 10)/70.0

		csv_writer.writerow([1, tract, time, sex, race, age])
	print "done!"




def str_to_time(s):
	""" Converts stop and frisk style date strings to time vector in [0, 1]"""
	if '-' in s: # format: 'yyyy-mm-dd' 
		year = int(s[:4])
		month = int(s[5:7])
		date = int(s[8:10])

	else: # format: 'mddyyy' or 'mmddyyyy'
		l = len(s)
		year = int(s[(l-4):])
		month = int(s[:(l-6)])
		date = int(s[(l-6):(l-4)])

	days = 365*(year-2003) + int(round(365.25/12*(month-1))) + (date-1)
	time = days/(365.25*11.9918)
	return time

def format_race(r):
	""" Converts race string to one of 4 standard options """
	if r == 'W':
		return r
	if r == 'B':
		return r
	if r in ['P', 'Q']:
		return 'H'
	else:
		return 'O'
if __name__ == '__main__':
	main()