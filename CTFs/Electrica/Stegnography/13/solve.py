from PIL import Image

im = Image.open("steg_1.gif")
data = list(im.getdata())
pix = im.load()
width, height = im.size

img = Image.new("L", im.size, "black")
pixels = img.load()
index = 0
for i in range(height) :
    for j in range(width) :
        if data[index] == 1 :
            pixels[j,i] = 0
        else :
            pixels[j,i] = 255
        index += 1
img.save("out.bmp")