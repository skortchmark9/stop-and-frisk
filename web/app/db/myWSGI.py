import pdb
import string
import sqlite3

#two APIs:
#search: http://localhost:8000/search;year=2003;eye=blue
#return the complete information of the corresponding dataset
#{year,frisked,searched,pct,datestop,timestop,sex,race,age,eyecolor,haircolr,build, xcoord, ycoord}

#http://localhost:8000/location?year=2003 &eye=blue
#return [{year,datestop,timestop,xcoord, ycoord}]

#http://localhost:8000/search?datestop=0827&timestop=2333

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    url=environ['PATH_INFO']
    print url
    requir_list=[]
    flag=-1
    if url.find('search')!=-1:
    	flag=0
    	requirments=url.split('search;')[1]
    	print requirments
    	requir_list=requirments.split(";")
    elif url.find('location')!=-1:
    	flag=1
    	requirments=url.split('location;')[1]
    	requir_list=requirments.split(";")
    else:
    	return "Command Error!"
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
    	c.execute(query, values)
    	resultset=c.fetchall()
    	c.close()

    if flag==1:
    	query = "select year,datestop,timestop,xcoord, ycoord from stop_and_frisked where"
    	for key in requir_dict:
    		query+=key+"=? and "
    		value_list.append(requir_dict[key])
    		values =tuple(value_list)

    	query = query.strip(" and ")
    	c = db.cursor()
    	c.execute(query, values)
    	resultset=c.fetchall()
    	c.close()

    db.commit()
    db.close()

    return resultset
