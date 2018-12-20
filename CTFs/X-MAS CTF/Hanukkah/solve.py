from Crypto.Util.number import isPrime
from random import getrandbits

def genKey(k):

	while True:
		r=getrandbits(k)
		while(r%2):
			r=getrandbits(k)
	
		p =  3 * r**2 +  2 * r + 7331
		q = 17 * r**2 + 18 * r + 1339
		n = p * q

		if(isPrime(p) and isPrime(q)):
			return (p,q) , n

def encrypt(m,pubkey):

	c=m**2 % pubkey
	return c

privkey,pubkey = genKey(256)

print privkey, pubkey