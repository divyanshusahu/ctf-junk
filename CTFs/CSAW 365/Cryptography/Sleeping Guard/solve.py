with open('out', 'rb') as f :
    data = f.read()

def xor(s,k) :
    m = ''
    for i in range(len(s)) :
        m += chr(ord(s[i]) ^ ord(k[i%len(k)]))
    return m

png_constant = '89504e470d0a1a0a0000000d'.decode('hex')
cipher = data[:12]
key = xor(png_constant, cipher)
print "Key = %s" % key

with open('flag.png', 'wb') as f :
    f.write(xor(data, key))