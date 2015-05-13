import cPickle

tracts = [s.strip() for s in open('tracts.txt').readlines()]
with open('tracts.pkl', 'wb') as fid:
	cPickle.dump(tracts, fid)  