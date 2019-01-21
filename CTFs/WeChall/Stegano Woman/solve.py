with open("stegano_woman.zip", "rb") as f :
    data = f.read()

extra = data[-264:]
cipher1 = extra.replace(" ","0").replace("\t", "1")
cipher2 = extra.replace(" ", "1").replace("\t", "0")

def bintoascii(s) :
    m = ""
    while s :
        c = s[:8]
        m += chr(int(c,2))
        s = s[8:]
    return m

print bintoascii(cipher1)
print bintoascii(cipher2)