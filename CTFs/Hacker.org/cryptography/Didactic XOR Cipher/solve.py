cipher = "3d2e212b20226f3c2a2a2b".decode("hex")
k = chr(79)
decipher = ""
for i in cipher :
    decipher += chr(ord(i)^ord(k))
print decipher