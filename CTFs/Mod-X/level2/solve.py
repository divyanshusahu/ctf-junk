def confirm(s) :
	for c in s :
		if ord(c) not in range(32,129) :
			return False
	return True

def shift(s,n) :
	data = ""
	for c in s :
		data += chr((ord(c)+n)%256)
	return data

with open("3nCryPt.enc","rb") as f :
	cipher = f.read()

result = shift(cipher, 232)
	#if confirm(result) :
	#	print i, result	
print result