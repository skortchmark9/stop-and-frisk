import csv
import cPickle


def main():
	census_to_precinct()

	complaints = {}

	with open('precincts.pkl', 'rb') as fid:
		precincts = cPickle.load(fid)

	for year in [2003, 2008, 2009]:
		f = 'complaints-' + str(year) + '-' + str(year + 4)
		lines = open(f).readlines()

		for line in lines:
			words = line.split()
			precinct = words[0].strip('st').strip('nd').strip('rd').strip('th')
			for i in range(5):
				key = (precinct, str(year + i))
				complaints[key] = words[i + 2]

	with open('complaints.pkl', 'wb') as fid:
		cPickle.dump(complaints, fid)  




def census_to_precinct():
	precincts_r = csv.reader(open('precinct_blocks_key.csv', 'rU'))
	precincts = {}
	for line in precincts_r:
		precincts[line[1]] = line[0]

	with open('precincts.pkl', 'wb') as fid:
		cPickle.dump(precincts, fid)  

if __name__ == '__main__':
	main()