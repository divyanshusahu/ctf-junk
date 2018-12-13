import base64

with open('eps.txt', 'rb') as f:
    cipher = f.read()

print base64.b64decode(cipher)