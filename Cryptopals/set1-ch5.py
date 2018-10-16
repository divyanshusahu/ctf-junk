def multiByteXor(string,key) :
	encodedSting = ''
	for i in range(len(string)) :
		encodedSting += chr(ord(string[i]) ^ ord(key[i%len(key)]))
	return encodedSting.encode('hex')

f = open('5.txt','r')
text = f.read().rstrip()
print multiByteXor(text,"ICE")