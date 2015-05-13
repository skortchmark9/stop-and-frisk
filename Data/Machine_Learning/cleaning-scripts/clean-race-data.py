import sys
import csv


def main():
	args = sys.argv
	if len(args) != 3:
		print 'Useage: clean-stop-and-frisk.py <data filename>\
		 <output filename>'
		return
	csv_reader = csv.reader(open(args[1], 'rU'))
	csv_writer = csv.writer(open(args[2], 'w'))
	csv_writer.writerow(['tract','total','white','black','hispanic','other'])

	for line in csv_reader:
		tract = line[0]
		white = int(line[1])
		black = int(line[2])
		hispanic = int(line[8])
		other = 0
		for i in range(3,7):
			other += int(line[i])
		total = white + black + hispanic + other
		d = float(total)
		csv_writer.writerow([tract, total, white/d, black/d, hispanic/d, other/d])


if __name__ == '__main__':
	main()