from base64 import b64decode
from Crypto.Cipher import AES

with open('10.txt', 'rb') as f :
	cipher = b64decode(f.read())

key = "YELLOW SUBMARINE"
IV = "\x00"*16

decrypt = AES.new(key, AES.MODE_CBC, IV)
message = decrypt.decrypt(cipher)
print message