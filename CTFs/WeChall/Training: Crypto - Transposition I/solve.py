with open('cipher.txt', 'r') as f :
    cipher = f.read()

decoded = ''
i = 0
while(i<len(cipher)) :
    decoded += cipher[i+1] + cipher[i]
    i += 2
print decoded