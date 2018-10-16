#!/usr/bin/python3

cipher = 'llkjmlmpadkkc'
key = 'thisisalilkey'
msg = ''

for i,j in zip(cipher, key) :
	msg += chr(((ord(i)-ord(j))%26)+97)

print(msg)