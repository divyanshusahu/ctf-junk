import gmpy

def factors_list(n) :
    fl = []
    for i in range(2,n/2+1) :
        if n%i == 0 :
            fl.append(i)
    return fl

bh = 666666*2
fl_bh = factors_list(bh)

for i in fl_bh :
    a = i
    b = bh/i
    c = a*a + b*b
    if gmpy.is_square(c) :
        c = int(c ** (0.5))
        print a,b,c
