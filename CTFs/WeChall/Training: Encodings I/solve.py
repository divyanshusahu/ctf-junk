with open('cipher.txt','rb') as f :
    cipher = f.read()
cipher = cipher.replace('\n','')
#print len(cipher)%56

x = cipher
message = ''
while(x) :
    cur = x[:7]
    message += chr(int(cur,2))
    x = x[7:]
print message