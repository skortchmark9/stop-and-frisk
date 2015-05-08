import pdb
import string
import sqlite3

url='/search;year=2004;datestop=0827;timestop=2333'
requir_list=[]
flag=-1
#pdb.set_trace()
if url.find('search')!=-1:
    flag=0
    #pdb.set_trace()
    requirments=url.split('search;')[1]
    requir_list=requirments.split(";")
elif url.find('location')!=-1:
    flag=1
    requirments=url.split('location;')[1]
    requir_list=requirments.split(";")
# else:
#     return ("Command Error!")
requir_dict={}
for item in requir_list:
    key=item.split("=")[0]
    value=item.split("=")[1]
    requir_dict[key]=value

db = sqlite3.connect('stop_and_frisked.db')

query=""
value_list=[]
resultset=()
if flag==0:
    query = "select * from stop_and_frisked where "
    for key in requir_dict:
        query+=key+"=? and "
    	value_list.append(requir_dict[key])
    	values =tuple(value_list)

    query = query.strip(" and ")
    c = db.cursor()
    #pdb.set_trace()
    c.execute(query, values)
    pdb.set_trace()
    resultset=c.fetchall()
    c.close()
    #pdb.set_trace()

if flag==1:
    query = "select year,datestop,timestop,xcoord,ycoord from stop_and_frisked where"
    for key in requir_dict:
    	query+=key+"=? and"
    	value_list.append(requir_dict[key])
    	values =tuple(value_list)

    query = query.strip(" and ")
    c = db.cursor()
    c.execute(query, values)
    resultset=c.fetchall()
    c.close()

db.commit()
db.close()
