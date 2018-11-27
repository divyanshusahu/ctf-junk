# breaking repeating multibyte key xor.

import base64

with open('6.txt', 'rb') as f :
	cipher = f.read()

cipher = base64.b64decode(cipher) # cipher in ascii

with open('6_cipher.txt', 'wb') as f :
	f.write(cipher)

def hamming_distance(s1, s2) :
	count = 0
	for i,j in zip(s1, s2) :
		if i != j :
			count += 1

	return count

def asciitobin(s) :
	result = ''
	for i in s :
		x = format(ord(i),'b')
		x = x.rjust(8,'0')
		result += x

	return result

def splitstring(s,n) :
	ss = []
	while(s) :
		x = s[:n]
		ss.append(x)
		s = s[n:]
	return ss

""" Key Length guessing (2-40) """

hds = {}

for keyLength in range(2,41) :
	hd = 0
	cl = splitstring(cipher,keyLength)

	for x in range(len(cl)-2) :
		hd += hamming_distance(cl[x], cl[x+1])

	hds[keyLength] = hd

actual_keyLength = min(hds, key=hds.get)
print "Key Length Guessed < %s >" % str(actual_keyLength) 

#print hamming_distance(asciitobin('this is a test'),asciitobin('wokka wokka!!!'))

""" Guessing the key """

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

cipher_blocks = {}

for i in range(actual_keyLength) :
	cipher_blocks[i] = ''

for i in range(len(cipher)) :
	cipher_blocks[i%actual_keyLength] += cipher[i]

actual_key = ''

for i in range(actual_keyLength) :
	c = cipher_blocks[i]
	maxScore = 0
	ak = ''
	for k in range(0,256) :
		ds = singleByteKeyXor(c, chr(k))
		score = scores(ds.lower())
		if score > maxScore :
			ak = chr(k)
			maxScore = score
	actual_key += ak

print "Guessed Key < %s >" % actual_key

print "\nDECODED MESSAGE\n"

def multiByteXor(string,key) :
	encodedString = ''
	for i in range(len(string)) :
		encodedString += chr(ord(string[i]) ^ ord(key[i%len(key)]))

	return encodedString

print multiByteXor(cipher, actual_key)