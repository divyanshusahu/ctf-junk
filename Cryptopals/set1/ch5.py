def multiByteXor(string,key) :
	encodedString = ''
	for i in range(len(string)) :
		encodedString += chr(ord(string[i]) ^ ord(key[i%len(key)]))
	return encodedString.encode('hex')

f = open('5.txt','r')
text = f.read().rstrip()
print multiByteXor(text,"ICE")