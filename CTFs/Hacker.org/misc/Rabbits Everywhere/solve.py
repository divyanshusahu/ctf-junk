a=1
b=1
index=2
s=0
while index<18 :
    c = a+b
    index += 1
    if index>=10 and index<=17 :
        s += c
    a = b
    b = c
print s