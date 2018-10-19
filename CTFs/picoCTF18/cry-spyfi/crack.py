#!/usr/bin/python2

from pwn import *
import string

def pad(message):
    if len(message) % 16 != 0:
        message = message + '0'*(16 - len(message)%16 )
    return message

sh = remote('2018shell1.picoctf.com', 34490)

sh.recvuntil(': ')

#inp = 'a'*(11) + 'icoCTF{@g3nt6_1$'
inp = 'a'*47
sh.sendline(inp)
#print inp

cipher = sh.recvline()[:-1]

print len(cipher)

agent_code = "*"*38

message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: {1}.
Down with the Soviets,
006
""".format( inp, agent_code )

print len(message)

message = pad(message)

#print len(cipher)
# not any input => size 320, that is 10 blocks

a1, c1 = message[:16], cipher[:32]
#print a1, c1

a2, c2 = message[16:32], cipher[32:64]
#print a2, c2

a3, c3 = message[32:48], cipher[64:96]
#print a3, c3

a4, c4 = message[48:64], cipher[96:128]
print a4,c4

a5, c5 = message[64:80], cipher[128:160]
print a5, c5

a6, c6 = message[80:96], cipher[160:192]
print a6, c6

a7, c7 = message[96:112], cipher[192:224]
print a7, c7

a8, c8 = message[112:128], cipher[224:256]
print a8, c8

a9, c9 = message[128:144], cipher[256:288]
print a9, c9

a10, c10 = message[144:160], cipher[288:320]
print a10, c10

a11, c11 = message[160:176], cipher[320:352]
print a11, c11

#print c5==c7
sh.close()

# 7b808bc6b0cfb7edec385bb5896648d4