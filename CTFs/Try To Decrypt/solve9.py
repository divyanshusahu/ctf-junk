import string

# backwards
symbols = "-_.,;:?! "
cipher = "6224F12C1C3FAA5AA54836B3C446D6415E74"

def divide_cipher(s) :
	l = []
	count = 0
	temp = ""
	for i in s :
		temp += i
		count += 1
		if count % 3 == 0 :
			l.append(temp)
			temp = ""
	return l

encrypt_lower = divide_cipher("4836B38E3A14C44E740B42E4415645875AA5CD5E060462764A66D6807A37C67E970D7208438668")
encrypt_upper = divide_cipher("898AC8CF8E290692994C96F982AA5AC8AEBA0FA22B45B68B8BBAEBC1CE4C08C2BC4EC61D84DA7D")
encrypt_digits = divide_cipher("0912C14F1622852A82CB2EE2023253")
encrypt_symbols = divide_cipher("CADEDD01E24E47E6AE8DEA0FC3F")

encrypt_dict = {}
for i,j in zip(string.lowercase, encrypt_lower) :
	encrypt_dict[i] = j

for i,j in zip(string.uppercase, encrypt_upper) :
	encrypt_dict[i] = j

for i,j in zip(string.digits, encrypt_digits) :
	encrypt_dict[i] = j

for i,j in zip(symbols, encrypt_symbols) :
	encrypt_dict[i] = j

"""def next_cipher(s) :
	c = ""
	c += hex((int(s[0],16)+2)%16)[2:]
	n = int(s[1],16)
	n += 3
	if n >= 16 :
		n = n%16
		c += hex(n)[2:]
		c += hex((int(s[2],16)+1)%16)[2:]
	else :
		c += hex(n)[2:]
		c += s[2]
	return c

def create_cipher_dict() :
	d = {}
	cur = "483"
	for i in string.lowercase :
		d[i] = cur
		cur = next_cipher(cur)
	return d

cipher_dict = create_cipher_dict()"""

message = ""

for i in divide_cipher(cipher) :
	try :
		message += encrypt_dict.keys()[encrypt_dict.values().index(i)]
	except :
		message += "*"

print message[::-1]