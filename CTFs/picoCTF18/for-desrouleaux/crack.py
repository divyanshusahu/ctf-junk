#!/usr/bin/python2

from pwn import *
import json
from sets import Set

sh = remote('2018shell1.picoctf.com',14079)

with open('incidents.json') as f :
	data = json.loads(f.read())

# question1 most common ip source address
source_ip = {}

for i in data[u'tickets'] :
	#print(i[u'src_ip'])
	if i[u'src_ip'] in source_ip :
		source_ip[i[u'src_ip']] += 1
	else :
		source_ip[i[u'src_ip']] = 1

#print(max(source_ip))
print(sh.recvuntil('ones.\n'))
sh.sendline(max(source_ip))

# question 2 How many unique ip add is tar by given src_ip
target = sh.recvuntil('?\n')
print(target)
target = str(target.split(' ')[-1])[:-2]

unq_dis = {}
for j in data[u'tickets'] :
	if j[u'src_ip'] == target :
		if j[u'dst_ip'] in unq_dis :
			unq_dis[j[u'dst_ip']] += 1
		else :
			unq_dis[j[u'dst_ip']] = 1

sh.sendline(str(len(unq_dis)))

print(sh.recvuntil('.\n'))

""" What is the average number of unique destination 
IP addresses that were sent a file with the same hash? 
Your answer needs to be correct to 2 decimal places."""

hashes = {}
for each in data[u'tickets'] :
	hash = each[u'file_hash']
	if hash not in hashes :
		hashes[hash] = Set()
	hashes[hash].add(each[u'dst_ip'])
#print(hashes)

avg = 0
for each in hashes :
	e = hashes[each]
#	print(e)
	avg += len(e)
#	print(avg)
avg = (avg*1.0)/ len(hashes)
#print(avg)
sh.sendline(str(avg))

sh.interactive()