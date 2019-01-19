cipher = "948881859781c4979186898d90c4c68c85878f85808b8b808881c6c4828b96c4908c8d97c4878c858888818a8381".decode("hex")

for i in range(256) :
    m = ""
    for j in cipher :
        m += chr(ord(j)^i)
    print i,m