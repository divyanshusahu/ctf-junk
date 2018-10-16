string1 = '1c0111001f010100061a024b53535009181c'.decode('hex')
string2 = '686974207468652062756c6c277320657965'.decode('hex')
decodedString = ''

for i,j in zip(string1,string2) :
	decodedString += chr(ord(i)^ord(j)).encode('hex')

print decodedString
