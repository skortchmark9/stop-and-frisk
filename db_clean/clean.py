import argparse
import json
import sys
import csv
import operator
import types  
import urllib2
import pdb

#python clean.py -csv_document data -json_file cleaned

# year:0
# datestop:3
# timestop:4
# frisked:22
# searched:23
# arstmade:14
# pct:1
# sex:80
# race:81
# age:83
# eyecolor:88
# haircolr:87
# build:89
# year 2003,2005 don't have data
# median income api seems doesn't work 
fieldnames = ("year","datestop","timestop","frisked",
	"searched","arstmade","pct","sex","race","age",
	"eyecolor","haircolr","build","xcoord","ycoord")

judgelist=["Y","N"]
racelist=["B","Q","I","W","Z"]
eyelist=["BR","BK","BL","XX","GR","HA"]
#BR(brown),BK(black),BL(blue),XX(unknown),GR(green),HA(hazel)
hairlist=["BK","BR","GY","WH","BL","XX","ZZ","SP","BA"]
#BK(black),BR(brown),GY(grey),WH(white),BL(blue),XX,ZZ,SP,BA
buildlist=["M","U","G","H"]

parser = argparse.ArgumentParser()
parser.add_argument('-csv_document', required=True, help='csv document')
parser.add_argument('-json_file', required=True, help='json file')
opts = parser.parse_args()
csv_document=opts.csv_document
json_file=opts.json_file

for i in range(3,15):
	flag=1
	file_path=csv_document+'/'+str(2000+i)+'.csv'
	csv_reader = csv.reader(open(file_path))
	jsonfile = open(json_file+'/'+str(2000+i)+'.json', 'wb+')
	jsonfile.write('[')
	for row in csv_reader:
#("FirstName","LastName","IDNumber","Message")
		year=row[0].strip()
		datestop=row[3].strip()
		if len(datestop)==7:
			datestop='0'+datestop
		timestop=row[4]
		if len(timestop)==3:
			timestop='0'+timestop
		if len(timestop.split(":"))>1:#some timestop are 0, 20 ,22:00
			time_list=timestop.split(":")
			timestop=timestop.split(":")
		class1=(3,4,5,7,8,9,10)
		class2=(11,12,13,14)
		if i in class1:#04,05,07,08,09,10
			frisked=row[22].strip()
			searched=row[23].strip()
			arstmade=row[14].strip()
			pct=row[1].strip()
			sex=row[79].strip()
			race=row[80].strip()
			age=row[82].strip()
			eyecolor=row[87].strip()
			haircolr=row[86].strip()
			build=row[88].strip()
			xcoord=row[106].strip()
			ycoord=row[107].strip()
		if i==6:
			datelist=datestop.split('-')
			if len(datelist)==3:
				datestop=datelist[1]+datelist[2]+datelist[0]
			frisked=row[22].strip()
			searched=row[23].strip()
			arstmade=row[14].strip()
			pct=row[1].strip()
			sex=row[83].strip()
			race=row[84].strip()
			age=row[86].strip()
			age=age[1:].strip()
			eyecolor=row[91].strip()
			haircolr=row[90].strip()
			build=row[92].strip()
			xcoord=row[109].strip()
			ycoord=row[110].strip()
			#pdb.set_trace()
		if i in class2:
			frisked=row[22].strip()
			searched=row[23].strip()
			arstmade=row[14].strip()
			pct=row[1].strip()
			sex=row[80].strip()
			race=row[81].strip()
			age=row[83].strip()
			eyecolor=row[88].strip()
			haircolr=row[87].strip()
			build=row[89].strip()
			xcoord=row[107].strip()
			ycoord=row[108].strip()

		if frisked in judgelist and searched in judgelist and arstmade in judgelist:
			#pdb.set_trace()#forceuse,row[79] not available in file 2003
			if race in racelist and eyecolor in eyelist and haircolr in hairlist and build in buildlist:
				if age!='99' and len(age)<3:
					if xcoord!=' ' and ycoord!=' ' and xcoord!='' and ycoord!='':
						#pdb.set_trace()
						xcoord=xcoord.strip()
						ycoord=ycoord.strip()
						if len(timestop)==4:
							if len(datestop)==8:
								if flag==0:
									data_string=','
								else:
									flag=0
									data_string=''
								datestop=datestop[0]+datestop[1]+datestop[2]+datestop[3]
								data_string += json.dumps({'year':year,'datestop':datestop,'timestop':timestop,'frisked':frisked,'searched':searched,'arstmade':arstmade,'pct':pct,'sex':sex,'race':race,'age':age,'eyecolor':eyecolor,'haircolr':haircolr,'build':build,'xcoord':xcoord,'ycoord':ycoord})
								data_string += '\n'
								jsonfile.write(data_string)
	jsonfile.write(']')

	