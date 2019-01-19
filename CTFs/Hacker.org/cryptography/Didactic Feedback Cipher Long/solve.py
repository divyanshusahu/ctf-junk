cipher = "e5534adac53023aaad55518ac42671f8a1471d94d8676ce1b11309c1c27a64b1ae1f4a91c73f2bfce74c5e8e826c27e1f74c4f8081296ff3ee4519968a6570e2aa0709c2c4687eece44a1589903e79ece75117cec73864eebe57119c9e367fefe9530dc1".decode("hex")
cipher_blocks = []
s = cipher
while s :
    cipher_blocks.append(s[:4])
    s = s[4:]

def xor(a,b) :
    m = ""
    for i in range(len(a)) :
        m += chr(ord(a[i])^ord(b[i]))
    return m

message = ""
for i in range(len(cipher_blocks)-1) :
    message += xor(cipher_blocks[i], cipher_blocks[i+1])
print message