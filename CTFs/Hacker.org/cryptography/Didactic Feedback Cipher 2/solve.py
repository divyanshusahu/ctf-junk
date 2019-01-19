cipher = "310a7718781f734c31425e775a314f3b40132c5122720599b2dfb790fd8ff894add2a4bdc5d1a6e987a0ed8eee94adcfbb94ee88f382127819623a404d3f".decode("hex")

for x in range(256) :
    m = ""
    for i in range(len(cipher)-1) :
        temp = ord(cipher[i+1]) ^ (ord(cipher[i])+x)%256
        if temp not in range(32,128) :
            continue
        else :
            m += chr(temp)
    if len(cipher)-1 == len(m) :
        print x,m