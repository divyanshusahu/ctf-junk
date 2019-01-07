from base64 import b64decode

cipher = 'RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS'
cipher = b64decode(cipher)
key = '\x03'
flag = ''
for c in cipher :
    flag += chr(ord(c)^ord(key))
print flag