with open('cipher.txt', 'rb') as f :
    cipher = f.read()

b1 = 'A'
b2 = 'B'

bacon_cipher = ''
for i in cipher :
    if ord(i) in range(65,91) :
        bacon_cipher += b1
    elif ord(i) in range(97,123) :
        bacon_cipher += b2
print bacon_cipher