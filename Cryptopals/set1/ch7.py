import base64
from Crypto.Cipher import AES

with open('7.txt','rb') as f:
	cipher = f.read()

cipher = base64.b64decode(cipher)

key = "YELLOW SUBMARINE"

message = AES.new(key, AES.MODE_ECB)
print message.decrypt(cipher)