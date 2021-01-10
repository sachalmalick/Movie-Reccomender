import csv
def read_csv(filename):
	l = []
	f = open(filename, "r")
	reader = csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
	for row in reader:
		l.append(tuple(row))
	return l