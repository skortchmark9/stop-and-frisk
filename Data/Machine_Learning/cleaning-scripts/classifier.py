from __future__ import division
import csv
import cPickle

import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

def bucket_time(time):
	time = float(time) - 0.24999971746607275
	size = (0.999998869864291-0.24999971746607275)/(9.0*12.0)
	bucket = int(time/size)
	return str(bucket)

def main():
	############################################################

	##### BUILD TRAINING SET ###################################

	# Load training text and training labels
	files = ['data/full-' + str(yr) + '.csv' for yr in range(2006, 2015)]
	files.append('population.csv')
	train_labels = []
	raw_features = []
	misses = 0
	positive = 0
	negative = 0
	for f in files:
		print 'Processing training data file: ', f
		reader = csv.reader(open(f, 'rU'))
		for line in reader:
			if len(line) != 6 or line[1] == "('', -1)" or float(line[2]) < 0: # error in the data set
				misses += 1
				continue
			label = int(line[0])
			if label == 1:
				positive += 1
			else:
				negative += 1
			train_labels.append(int(line[0]))
			feature_dict = {}
			feature_dict['tract'] = str('{0:09d}'.format(int(line[1])))
			feature_dict['time'] = bucket_time(line[2])
			feature_dict['sex'] = line[3]
			feature_dict['race'] = line[4]
			feature_dict['age'] = (int(line[5]) - 10)/70.0
			raw_features.append(feature_dict)

	average = positive / float(positive + negative)
	print 'Number positive = ', positive
	print 'Number negative = ', negative
	print 'Number of errors = ', misses
	print 'Average rate = ', average

	with open('saved_average.pkl', 'wb') as fid:
	    cPickle.dump(average, fid)  

	# Get training features using vectorizer
	vectorizer = DictVectorizer(sparse=True) 
	train_features = vectorizer.fit_transform(raw_features)
	print 'Training feature matrix size: ', train_features.shape

	with open('saved_vectorizer.pkl', 'wb') as fid:
	    cPickle.dump(vectorizer, fid) 
	
	# # Transform training labels to numpy array (numpy.array)
	train_labels = np.array(train_labels)
	
	# ############################################################


	# ##### TRAIN THE MODEL ######################################
	# Initialize the corresponding type of the classifier and train it (using 'fit')
	classifier = LogisticRegression()
	classifier.fit(train_features, train_labels)
	# ############################################################


	# ###### VALIDATE THE MODEL ##################################
	# # Print training mean accuracy using 'score'
	print 'Training mean accuracy score: ', classifier.score(train_features, train_labels)
	
	# save the classifier
	with open('saved_classifier.pkl', 'wb') as fid:
	    cPickle.dump(classifier, fid)    
	
	# ############################################################


	# ##### EXAMINE THE MODEL ####################################
	# if opts.top is not None:
	# 	# print top n most informative features for positive and negative classes
	# 	util.print_most_informative_features(opts.classifier, vectorizer, classifier, opts.top)
	# ############################################################


	# ##### TEST THE MODEL #######################################
	print 'White female test over time:'
	for t in range(1,100):
		test_dict = {'tract': '005006800', 'time': bucket_time(str(t*0.01)), 'race': 'W', 'age': 0.2}

		test_features = vectorizer.transform([test_dict])
		# Print the predicted label of the test 
		probs = classifier.predict_proba(test_features)[0]
		rel_prob = probs[1]/average
		print '\tRelative probability: {0:.2f}'.format(rel_prob), 'times as likely'



	print 'Black male test:'
	test_dict = {'tract': '81146300', 'time': bucket_time('0.07'), 'sex': 'M', 'race': 'B', 'age': 0.2}

	test_features = vectorizer.transform([test_dict])

	probs = classifier.predict_proba(test_features)[0]
	rel_prob = probs[1]/average
	print '\tRelative probability: {0:.2f}'.format(rel_prob), 'times as likely'

 		
if __name__ == '__main__':
	main()
