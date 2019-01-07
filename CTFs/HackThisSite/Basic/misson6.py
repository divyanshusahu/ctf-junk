s = '08fh5j=?'
d = ''
for n in range(len(s)):
	d += chr(ord(s[n])-n)
print d
