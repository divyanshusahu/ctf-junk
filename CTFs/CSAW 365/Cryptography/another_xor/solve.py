#!/usr/bin/python2
with open('ciphertext.txt', 'rb') as f:
    cipher = f.read()

cipher = cipher.decode('hex')
#print len(cipher)

def xor(s, k) :
    cipher = ''
    for i in range(len(s)) :
        cipher += chr(ord(s[i]) ^ ord(k[i%len(k)]))
    return cipher

print "\ncipher format = plaintext + key + md5(plaintext+key)"
c1, c2 = cipher[:105], cipher[105:]

print "Let assume that plaintext is of the form flag{****}"
key = xor(cipher[:5], 'flag{')
print "Initials characters of the key is < %s >" % key

print "No repetition, so the minimum length of key is 5."
print "Since we know that after decryption the last 32 chars contains a md5 hash. That is only hex characters."
print "Therefore we try to guess key length."
print "Minimum length of plaintext is six, therefore upper bound on key length is 99."

hash_chars = '0123456789abcdef'
probable_keylength = []
for i in range(1,95) :
    k = key + '*'*i
    temp_key_length = len(k)
    temp_plaintext = xor(cipher, k)
    temp_hash = temp_plaintext[105:]
    place = {}
    for j in range(105,137) :
        if (j%temp_key_length) < 5 :
            place[j] = key[j%temp_key_length]
    #print place
    success = 1
    for x in place :
        if chr( ord(cipher[x]) ^ ord(place[x]) ) not in hash_chars :
            success = 0
            break
    if success and place :
        probable_keylength.append(temp_key_length)

print "\nProbable key lengths =", probable_keylength
keylength = 67

actual_key = [None] * keylength
message = [None] * 105

actual_key[0] = 'A'
actual_key[1] = ' '
actual_key[2] = 'q'
actual_key[3] = 'u'
actual_key[4] = 'a'

message[0] = 'f'
message[1] = 'l'
message[2] = 'a'
message[3] = 'g'
message[4] = '{'

for i in range(38,43) :
    message[i] = actual_key[i-38]

while(None in actual_key) :
    for i in range(38, len(message)) :
        if message[i] :
            actual_key[i%keylength] = chr(ord(message[i]) ^ ord(cipher[i]))
            message[(i%keylength)+38] = chr(ord(message[i]) ^ ord(cipher[i]))

key = ''
for y in actual_key :
    key += y

print "Key = %s" % key

plaintext = xor(cipher, key)
print "Plaintext = %s " % plaintext