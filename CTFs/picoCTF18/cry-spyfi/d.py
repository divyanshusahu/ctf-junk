#!/usr/bin/python2

from pwn import *
import string

flag1 = ''
check = ''

for i in range(1,39) :
	sh = remote('2018shell1.picoctf.com', 34490)
	if i <= 28 :
		ip = 'a' * (28-i)
	else :
		ip = 'a'*(48-(i-28))
	sh.recvuntil(': ')
	sh.sendline(ip)
	cipher = sh.recvline()
	#print cipher
	if i <=28 :
		check = cipher[192:224]
	else :
		check = cipher[288:320]
	sh.close()
	for j in string.printable :
		cipher = ''
		sh = remote('2018shell1.picoctf.com', 34490)
		sh.recvuntil(': ')
		temp = 'fying code is: '
		if len(flag1) >= 16 :
			temp_flag = flag1[-15:]
		else :
			temp_flag = flag1
		inp = 'a'*(11) + temp[i-1:] + temp_flag + j
		#print inp[11:]
		print i, 'Trying ' + j 
		sh.sendline(inp)
		cipher = sh.recvline()[:-1]
		c5 = cipher[128:160]
		#print c5, check
		if c5 == check :
			flag1 += j
			sh.close()
			break
		sh.close()
	print flag1

print '========== Flag Found =========='
print flag1