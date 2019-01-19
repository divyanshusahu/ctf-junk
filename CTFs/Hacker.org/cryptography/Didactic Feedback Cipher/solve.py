cipher = "751a6f1d3d5c3241365321016c05620a7e5e34413246660461412e5a2e412c49254a24".decode("hex")

m = ""
for i in range(len(cipher)-1) :
    m += chr(ord(cipher[i])^ord(cipher[i+1]))
print m