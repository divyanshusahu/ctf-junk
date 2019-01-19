cipher = "31cf55aa0c91fb6fcb33f34793fe00c72ebc4c88fd57dc6ba71e71b759d83588".decode("hex")

for b in range(256) :
    key = b
    for x in range(256) :
        m = ""
        for c in cipher :
            cur = chr(ord(c) ^ key)
            key = (key+x)%256
            if ord(cur) not in range(32,128) :
                continue
            else :
                m += cur
        if len(m) == len(cipher) :
            print b,x,m
