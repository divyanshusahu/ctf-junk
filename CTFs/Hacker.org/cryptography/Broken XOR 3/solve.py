cipher = "8d541ae26426f8b97426b7ae7240d78e401f8f904717d09b2fa4a4622cfcbf7337fbba2cdbcb4e3cdb994812b66a27e9e02f21faf8712bd2907fc384564998857e3b1"
temp = cipher
cipher_blocks = []
while temp :
    cipher_blocks.append(temp[:2])
    temp = temp[2:]
#print cipher_blocks
t = cipher[:len(cipher)-19].decode("hex")
#print t

for b in range(256):
    key = b
    for x in range(256):
        m = ""
        for c in t:
            cur = chr(ord(c) ^ key)
            key = (key+x) % 256
            if ord(cur) not in range(32, 128):
                continue
            else:
                m += cur
        if len(m) == len(t):
            print b, x, m