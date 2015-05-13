import sys
import csv


def main():
	args = sys.argv
	if len(args) != 3:
		print 'Useage: clean-age-data.py <data filename>\
		 <output filename>'
		return
	csv_reader = csv.reader(open(args[1], 'rU'))
	csv_writer = csv.writer(open(args[2], 'w'))

	for line in csv_reader:
		if 'Tract' in line[0]:
			row = ['tract', 'total']
			for i in range(2,13):
				row.append('f:' + line[i].split()[0])
			for i in range(13, 25):
				row.append('m:' + line[i].split()[0])
			csv_writer.writerow(row)
			continue
		total = 0
		nums = []
		for i in range(1, 25):
			n = int(line[i].replace(',',''))
			nums.append(n)
			total = total + n
		d = float(total)
		row = [line[0]]
		if d > 0:
			row.append(total)
			for n in nums:
				row.append(n/d)
		else:
			row.append(0)
		csv_writer.writerow(row)




if __name__ == '__main__':
	main()