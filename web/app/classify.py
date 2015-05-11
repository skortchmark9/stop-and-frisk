from __future__ import division
import sys
import csv
import argparse
import cPickle
from collections import defaultdict
from conversion import census_9_to_census_7
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

def main():

	test_dict = {'time': '01012013', 'sex': 'M', 'race': 'B', 'age': '17'}
	get_probs_all_tracts(test_dict)


def get_probs_all_tracts(feature_dict):
 	with open('web/app/Classifier/saved_classifier.pkl', 'rb') as fid:
		classifier = cPickle.load(fid)

	with open('web/app/Classifier/saved_vectorizer.pkl', 'rb') as fid:
		vectorizer = cPickle.load(fid)

	with open('web/app/Classifier/saved_average.pkl', 'rb') as fid:
		average = cPickle.load(fid)

	with open('web/app/Classifier/tracts.pkl', 'rb') as fid:
		tracts = cPickle.load(fid)

	feature_dict['time'] = str_to_time(feature_dict['time'])
	feature_dict['age'] = (int(feature_dict['age']) - 10)/70.0

	prob_dict = {}

	for tract in tracts:
		if len(tract) == 7:
			tract = '0' + tract

		tract = census_9_to_census_7(tract)

		tract_dict = feature_dict
		tract_dict['tract'] = str('{0:09d}'.format(int(tract)))

		features = vectorizer.transform([tract_dict])

		probs = classifier.predict_proba(features)[0]
		prob_dict[tract] = probs[1]/average
	return prob_dict

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

if __name__ == '__main__':
	main()
