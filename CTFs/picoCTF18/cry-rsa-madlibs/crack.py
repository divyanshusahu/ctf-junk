from pwn import *

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def untilnum(a) :
	num_r = ['0','1','2','3','4','5','6','7','8','9']
	num = ''
	for i in a :
		if i in num_r :
			num += i
		else :
			return int(num)

sh = remote('2018shell1.picoctf.com', 18148)

d1 = sh.recvuntil('(Y/N):')
#print(d1)
q1 = int(d1.split(' : ')[-2][:-2])
p1 = int(d1.split(' : ')[-1][:5])
#print(q,p)

sh.sendline('y')
sh.sendline(str(p1*q1))
print('Question 1 Done!')

d2 = (sh.recvuntil('(Y/N)'))
#print(d2)
#print(d2.split(' : '))
p2 = int(d2.split(' : ')[1][:5])
n2 = int(d2.split(' : ')[2][:10])
#print(p2,n2)

if n2%p2 == 0 :
	sh.sendline('y')
	sh.sendline(str(n2/p2))
else :
	sh.sendline('n')
print('Question 2 Done!')

d3 = sh.recvuntil('(Y/N)')
#print(d3)
e3 = d3.split(' : ')[1][:1]
n3 = untilnum(d3.split(' : ')[2])

try :
	modinv(n3,e3)
	sh.sendline('y')
except :
	sh.sendline('n')
print('Question 3 Done!')

d4 = sh.recvuntil('(Y/N)')
q4 = untilnum(d4.split(' : ')[1])
p4 = untilnum(d4.split(' : ')[2])
t4 = (p4-1)*(q4-1)
sh.sendline('y')
sh.sendline(str(t4))
print('Question 4 Done!')

d5 = sh.recvuntil('(Y/N)')
p5 = untilnum(d5.split(' : ')[1])
e5 = untilnum(d5.split(' : ')[2])
n5 = untilnum(d5.split(' : ')[3])
sh.sendline('y')
c5 = pow(p5,e5,n5)
sh.sendline(str(c5))
print('Question 5 Done!')

d6 = sh.recvuntil('(Y/N)')
c6 = untilnum(d6.split(' : ')[1])
e6 = untilnum(d6.split(' : ')[2])
n6 = untilnum(d6.split(' : ')[3])
sh.sendline('n')
print('Question 6 Done!')

d7 = sh.recvuntil('(Y/N)')
q7 = untilnum(d7.split(' : ')[1])
p7 = untilnum(d7.split(' : ')[2])
e7 = untilnum(d7.split(' : ')[3])

try :
	de7 = modinv(e7, (p7-1)*(q7-1))
	sh.sendline('y')
	sh.sendline(str(de7))
except :
	sh.sendline('n')
print('Question 7 Done!')

d8 = sh.recvuntil('(Y/N)')
p8 = untilnum(d8.split(' : ')[1])
c8 = untilnum(d8.split(' : ')[2])
e8 = untilnum(d8.split(' : ')[3])
n8 = untilnum(d8.split(' : ')[4])

if n8 % p8 == 0 :
	sh.sendline('y')
	q8 = n8/p8
	de8 = modinv(e8, (p8-1)*(q8-1))
	m8 = pow(c8,de8,n8)
	sh.sendline(str(m8))
else :
	sh.sendline('n')
print('Question 8 Done!')

flag = str(hex(m8))[2:].decode('hex')
print(flag)