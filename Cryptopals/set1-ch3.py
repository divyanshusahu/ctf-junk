freq = {}
freq[' '] = 700000000
freq['e'] = 390395169
freq['t'] = 282039486
freq['a'] = 248362256
freq['o'] = 235661502
freq['i'] = 214822972
freq['n'] = 214319386
freq['s'] = 196844692
freq['h'] = 193607737
freq['r'] = 184990759
freq['d'] = 134044565
freq['l'] = 125951672
freq['u'] = 88219598
freq['c'] = 79962026
freq['m'] = 79502870
freq['f'] = 72967175
freq['w'] = 69069021
freq['g'] = 61549736
freq['y'] = 59010696
freq['p'] = 55746578
freq['b'] = 47673928
freq['v'] = 30476191
freq['k'] = 22969448
freq['x'] = 5574077
freq['j'] = 4507165
freq['q'] = 3649838
freq['z'] = 2456495

def singleByteKeyXor(encodedString,key) :
	decodedString = ''
	for i in encodedString :
		decodedString += chr(ord(i) ^ ord(key))
	return decodedString

def scores(decodedString) :
	score = 0
	for i in decodedString :
		try :
			score += freq[i]
		except :
			continue
	return score

hexEncodedString = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
string = hexEncodedString.decode('hex')
maxScore = 0
actualString = ''
actualKey = ''

for key in range(256) :
	decodedString = singleByteKeyXor(string,chr(key))
	score = scores(decodedString)
	if score > maxScore :
		maxScore = score
		actualKey = chr(key)
		actualString = decodedString

print actualKey, actualString

#listDict = {
#	'e':12.49,
#	't':9.28,
#	'a':8.04,
#	'o':7.64,
#	'i':7.57,
#	'n':7.23,
#	's':6.51,
#	'r':6.28,
#	'h':5.05,
#	'l':4.07,
#	'd':3.82,
#	'c':3.34,
#	'u':2.73,
#	'm':2.51,
#	'f':2.40,
#	'p':2.14,
#	'g':1.87,
#	'w':1.68,
#	'y':1.66,
#	'b':1.48,
#	'v':1.05,
#	'k':0.54,
#	'x':0.23,
#	'j':0.16,
#	'q':0.12,
#	'z':0.09
#}