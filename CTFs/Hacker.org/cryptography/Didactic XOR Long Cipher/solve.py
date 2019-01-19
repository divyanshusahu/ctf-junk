cipher = "8776459cf37d459fbb7b5ecfbb7f5fcfb23e478aaa3e4389f378439aa13e4e96a77b5fc1f358439df36a4486a03e4381b63e5580a66c0c8ebd6d5b8aa13e459cf34e4d9fa67f02cf90714288a17f589abf7f5886bc705fcfbc700c96bc6b5ecfb7775f8cbc68499daa3f".decode("hex")

def xor(s,k) :
    m = ''
    for i in range(len(s)) :
        m += chr(ord(s[i])^ord(k[i%len(k)]))
    return m

key = ""
msg = "This"
for i in range(4) :
    key += chr(ord(cipher[i])^ord(msg[i]))

print xor(cipher,key)