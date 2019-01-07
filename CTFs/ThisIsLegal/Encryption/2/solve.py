def decode(s,k) :
    msg = ""
    c = 0
    for i in range(len(s)) :
        if s[i] == " " :
            msg += " "
            continue
        msg += chr(((ord(s[i]) - ord(k[c%len(k)]))%26)+96)
        c += 1
    return msg

cipher = "Rwfwcvttw ufriifyg dws jjbhwooqm ezu iwsh".lower()
key = "enc"
print decode(cipher, key)