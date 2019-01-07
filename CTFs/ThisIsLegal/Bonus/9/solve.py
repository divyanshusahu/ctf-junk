s = "41 63 01 01 82 21 63 03 41"
d = s.split(" ")
e = []
for i in d :
    e.append(i[::-1])
print e
msg = ''
for i in e :
    msg += chr(int(i)/2 + 96)
print msg