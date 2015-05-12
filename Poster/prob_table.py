import sys
import numpy
from random import randint
sys.path.insert(0, 'web/app')

from classify import get_probs_all_tracts


def avg_tract(tract_data):
	values = list(tract_data.values())
	avg = numpy.mean(values)
	return avg
test_dict = {'time': '01012013', 'sex': 'M', 'race': 'B', 'age': '20'}

times = []

for year in range(2006, 2015):
	str_year = str(year)
	for i in range(0,10):
		month = randint(1,12)
		if month < 10:
			month = "0" + str(month)
		else:
			month = str(month)
		day = randint(1,20)
		if day < 10:
			day = "0" + str(day)
		else:
			day = str(day)
		times.append(month+day+str_year)
		

sexes = ['M', 'F']
races = ['B', 'W', 'H', 'O']

result = numpy.zeros(shape=(len(races), len(sexes)))

age_range = [20, 61, 10]

for si, sex in enumerate(sexes):
	for ri, race in enumerate(races):
		for age in age_range:
			for time in times:
				query = {'time': time, 'sex': sex, 'race': race, 'age': str(age)}
				result[ri][si] += avg_tract(get_probs_all_tracts(query))/(len(age_range)*len(times))
				print result

row_format ="{:15}" * (len(sexes) + 1)
print row_format.format("", *sexes)
for r, row in zip(races, result):
	print row_format.format(r, *row)


#print get_probs_all_tracts(test_dict)
