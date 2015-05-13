import sys
import csv


def main():
	args = sys.argv
	if len(args) != 4:
		print 'Useage: clean-stop-and-frisk.py <data filename>\
		 <output filename> <attribute list filename>'
		return
	csv_reader = csv.reader(open(args[1], 'rU'))
	csv_writer = csv.writer(open(args[2], 'w'))
	attributes = [int(line)-1 for line in open(args[3]).readlines()]

	for line in csv_reader:
		row = []
		skip = False
		for a in attributes:
			if line[a] == ' ':
				skip = True
				break
			if a == 82 and line[a] != 'age': # age attribute
				age = line[a]
				if age == '**' or age == 'detail1_' or int(age) < 10 or int(age) > 94:
					skip = True
					break
			row.append(line[a])
		if not skip: 
			csv_writer.writerow(row)




if __name__ == '__main__':
	main()