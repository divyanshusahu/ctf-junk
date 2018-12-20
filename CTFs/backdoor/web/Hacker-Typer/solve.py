f = open('a.txt', 'r')

for i in f.readlines() :
	print i.rstrip().decode('hex')