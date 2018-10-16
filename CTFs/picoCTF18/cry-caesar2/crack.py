with open('ciphertext') as f :
	data = f.read()

r = range(0,128)

for i in r :
	x = chr((ord(data[0]) + i)%128)
	if x == 'p' :
		k=i

msg = ''
for c in data :
	m = ord(c) + 60
	if m > 128 :
		m = m-127
		m += 33
	msg += chr(m)

print(msg)