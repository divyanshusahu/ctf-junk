import gmpy

s = 0
for i in range(1,2119) :
    if gmpy.is_square(i) :
        s += i*2
    else :
        s += i
print s