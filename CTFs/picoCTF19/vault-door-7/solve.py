def bin2ascii(s) :
    ans = ""
    temp = s
    while(temp) :
        x = temp[:8]
        x = int(x,2)
        ans += chr(x)
        temp = temp[8:]
    
    return ans

x = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734304870, 895891557, 1681142832]

password = ""

for i in x :
    temp = bin(i)[2:]
    temp = temp.zfill(32)
    password += bin2ascii(temp)

print(password)
