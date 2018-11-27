def splitstring(s,n) :
	ss = []
	while(s) :
		x = s[:n]
		ss.append(x)
		s = s[n:]
	return ss

f = open('8.txt', 'r')
count = 0

for i in f.readlines() :
	c = i.rstrip()
	count += 1
	s = splitstring(c,32)
	ss = set(s)
	if len(s) != len(ss) : # AES in ECB mode has has cipher text for the same message
		print count

f.close()