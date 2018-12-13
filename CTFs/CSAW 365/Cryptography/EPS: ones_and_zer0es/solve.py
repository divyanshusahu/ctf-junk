with open('eps.txt', 'rb') as f :
    cipher = f.read()

def convert_bin_to_ascii(s) :
    x = s
    msg = ''
    while(x) :
        cur = x[:8]
        msg += chr(int(cur, 2))
        x = x[8:]
    return msg

print convert_bin_to_ascii(cipher)