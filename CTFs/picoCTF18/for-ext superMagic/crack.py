#!/usr/bin/python2

with open('ext-super-magic.img', 'rb') as f :
	data = f.read()

d1 = data[:1024+56]
magic_number = '53EF'.decode('hex')
d2 = data[1024+56+2:]

with open('new.img', 'wb') as f :
	f.write(d1+magic_number+d2)