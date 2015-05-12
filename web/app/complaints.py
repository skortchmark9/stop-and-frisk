import cPickle

def main():
	print get_complaints()	

def get_complaints():
	with open('web/app/static/data/precincts.pkl', 'rb') as fid:
		precincts = cPickle.load(fid)

	with open('web/app/static/data/complaints.pkl', 'rb') as fid:
		complaints = cPickle.load(fid)

	with open('web/app/Classifier/tracts.pkl', 'rb') as fid:
		tracts = cPickle.load(fid)

	comp_dict = {}
	prefixes = {'047':'3','061':'1','005':'2','081':'4','085':'5'}
	for tract in tracts: 
		tract = "{0:0>9}".format(tract)
		t = prefixes[tract[:3]] + tract[3:]

		pre = precincts[tract]
		comps = []
		for year in range(2003, 2014):
			key = (pre, str(year))
			if pre == '':
				comps.append('N/A')
			else:
				comps.append(complaints[key])
		comps.append('N/A')
		comp_dict[t] = comps
	return comp_dict

if __name__ == '__main__':
	main()	


