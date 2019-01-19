keyStr = "ABCDEFGHIJKLMNOP"+"QRSTUVWXYZabcdef"+"ghijklmnopqrstuv"+"wxyz0123456789+/"+"="
cipher = "cXVlZW4lMjdzJTIwZ2FtYml0"
message = ""

def encodeIt(inp) :
    output = ""
    chr1 = chr2 = chr3 = ""
    enc1 = enc2 = enc3 = enc4 = ""
    i = 0
    while i < len(inp) :
        chr1 = ord(inp[i])
        i+=1
        chr2 = ord(inp[i])
        i+=1
        chr3 = ord(inp[i])
        i+=1

        enc1 = chr1 >> 2
        enc2 = ((chr1 & 3) << 4) | (chr2 >> 4)
        enc3 = ((chr2 & 15) << 2) | (chr3 >> 6)
        enc4 = chr3 & 63

        t2 = unicode(str(chr2),'utf-8')
        t3 = unicode(str(chr3),'utf-8')

        if t2.isnumeric() == False :
            enc3 = enc4 = 64
        elif t3.isnumeric() == False :
            enc4 = 64

        output += keyStr[enc1] + keyStr[enc2] + keyStr[enc3] + keyStr[enc4]
    return output

with open("a.txt", "rb") as f :
    data = f.readlines()

t = cipher
while t :
    cur = t[:4]
    for line in data :
        l = line.rstrip()
        if encodeIt(l) == cur :
            message += l
            break
    print message
    t = t[4:]
