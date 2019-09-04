with open("data.dat", "rb") as f :
	data = f.readlines()

count = 0

for line in data :
	line = line.rstrip()
	#print line
	#break
	x0 = line.count("0")
	x1 = len(line) - x0
	if x0 % 3 == 0 :
		count += 1
	elif x1 % 2 == 0 :
		count += 1

print count
