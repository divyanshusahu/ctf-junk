with open('pimitive', 'rb') as f :
    data = f.read()

magic_number = "504B0304".decode('hex')
"""key = ''
for i in range(4) :
    key += chr( ord(data[i]) ^ ord(magic_number[i]) )
print key, len(data)"""

def xor(c,k) :
    message = ''
    for i in range(len(c)) :
        message += chr( ord(c[i]) ^ ord(k[i%len(k)]) )
    return message

with open('key.txt','rb') as f :
    key = f.read()

key = key.replace(' ','')
print len(key), len(data)

msg = xor(data, key)
with open('out', 'wb') as f :
    f.write(msg)