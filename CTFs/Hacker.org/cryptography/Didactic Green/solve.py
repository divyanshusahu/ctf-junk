from PIL import Image

im = Image.open("greenline.png")
data = list(im.getdata())
width, height = im.size
s = ""

for i in data :
    s += chr(i[1])
print s