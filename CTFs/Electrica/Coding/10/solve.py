a = 0
b = 1
index = 2
while True :
    c = a + b
    index += 1
    if c % (2**32) == 0 :
        print c, index
        break

    a = b
    b = c