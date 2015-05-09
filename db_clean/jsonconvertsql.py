import json
import sqlite3
import pdb

db = sqlite3.connect('stop_and_frisked.db')

for i in range(3,15):
	name='data/'+str(2000+i)+'.json'
	#pdb.set_trace()
	traffic = json.load(open(name))
	query = "insert into stop_and_frisked values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
	#pdb.set_trace()
	columns = ["year","datestop","timestop","frisked","searched","arstmade","pct","sex","race","age","eyecolor","haircolr","build","xcoord","ycoord"]
	if traffic!=[]:
		#pdb.set_trace()
		for data in traffic:
			#pdb.set_trace()
			keys =tuple(data[c] for c in columns)
			c = db.cursor()
			c.execute(query, keys)
			c.close()

db.commit()
db.close()