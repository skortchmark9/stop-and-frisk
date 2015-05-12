import json
import sqlite3
import pdb
from conversion import state_2_lat_lng

db = sqlite3.connect('stop_and_frisked.db')
db1 = sqlite3.connect('stop_and_frisked_v01.db')

#pdb.set_trace()
columns = ["year","datestop","timestop","frisked","searched","arstmade","pct","sex","race","age","eyecolor","haircolr","build","xcoord","ycoord"]

cur = db.cursor()
query1 = "select * from stop_and_frisked"
cur.execute(query1)
res = cur.fetchall()


cur1 = db1.cursor()
query = "insert into stop_and_frisked values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
for line in res:
	#pdb.set_trace()
	if line[0].strip()!='2004' and line[0].strip()!='2005':
		(a,b)=state_2_lat_lng(float(line[13]),float(line[14]))
		keys=tuple([line[0].strip(),line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],a,b])
		cur1.execute(query, keys)
cur.close()
cur1.close()

db.commit()
db.close()
db1.commit()
db1.close()