with open('cipher.txt', 'rb') as f:
    cipher = f.read()

cipher = cipher.replace('\n','')
cipher = cipher.replace(' ','')
cipher = cipher.decode('hex')

for i in range(1,127) :
    message = ''
    f = 0
    for j in cipher :
        if ord(j) == 32 :
            continue
        cur = (ord(j) + i) % 128
        if cur < 32 :
            f = 1
        message += chr(cur)
    if f == 1 :
        continue
    print i, message
print cipher