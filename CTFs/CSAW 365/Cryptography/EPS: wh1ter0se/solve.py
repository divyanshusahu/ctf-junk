with open('eps1.txt', 'rb') as f :
    cipher = f.read()

def shift(s, k) :
    text_range = range(65,91)
    msg = ''
    for i in s :
        if ord(i) in text_range :
            cur = ord(i) - 65
            n = (cur+k) % 26
            n += 65
            msg += chr(n)
        else :
            msg += i
    return msg

for k in range(1,26) :
    print shift(cipher, k)

# This is substitution cipher, solved in quipquip.com