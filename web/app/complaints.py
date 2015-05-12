import cPickle

def main():
	print get_complaints('5000100', '2003')	

def get_complaints(tract, year):
	tract = "{0:0>9}".format(tract)
	with open('web/app/static/data/precincts.pkl', 'rb') as fid:
		precincts = cPickle.load(fid)

	with open('web/app/static/data/complaints.pkl', 'rb') as fid:
		complaints = cPickle.load(fid)

	pre = precincts[tract]
	key = (pre, year)
	return complaints[key]

if __name__ == '__main__':
	main()	


