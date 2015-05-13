import itertools
import csv
import random as r
import numpy.random as npr


def main():
	race_r = csv.reader(open('full-race-by-census-tract.csv', 'rU'))
	sex_age_r = csv.reader(open('full-sex-age-by-census-tract.csv', 'rU'))
	csv_writer = csv.writer(open('population.csv', 'w'))
	csv_writer.writerow(['tract','total','white','black','hispanic','other'])
	factor = 2

	for r_line, s_line in itertools.izip(race_r, sex_age_r):
		if r_line[0] == 'tract' or r_line[1] == '0': 
			continue
		tract = r_line[0]

		races = ['W', 'B', 'H', 'O'] 
		race_weights = [float(r_line[2]), float(r_line[3]), float(r_line[4]), float(r_line[5])]

		for i in range(2, 14):
			num_cit = int(s_line[i])/factor
			for x in range(num_cit):			
				age = r.randint(i*5, i*5+4)
				race = npr.choice(races, p=race_weights)
				time = r.uniform(0.24999971746607275, 0.999998869864291)
				csv_writer.writerow([0, tract, time, 'F', race, age])
				
		for i in range(14, 26):
			num_cit = int(s_line[i])/factor
			for x in range(num_cit):
				age = r.randint((i-12)*5, (i-12)*5+4)
				race = npr.choice(races, p=race_weights)
				time = r.uniform(0.24999971746607275, 0.999998869864291)
				csv_writer.writerow([0, tract, time, 'M', race, age])



if __name__ == '__main__':
	main()