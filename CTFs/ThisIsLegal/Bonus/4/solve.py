from PIL import Image

im = Image.open('img.bmp','r')
pix = im.load()
width, height = im.size

for i in range(height) :
    for j in range(width) :
        r,g,b = pix[j,i]
        if (r,g,b) != (0,0,0) :
            pix[j,i] = 255,255,255
im.save('solve.bmp')
