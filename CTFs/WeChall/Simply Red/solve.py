from PIL import Image
import gmpy

im = Image.open("op.png")
data = list(im.getdata())
pix = im.load()
width, height = im.size

for i in range(height) :
    for j in range(width) :
        r = pix[j,i][0]
        if gmpy.is_prime(r) != 0 :
            pix[j,i] = 0,255,0
        else :
            pix[j,i] = 0,0,0
im.save("out.png")