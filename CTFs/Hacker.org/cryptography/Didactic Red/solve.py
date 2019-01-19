from PIL import Image

im = Image.open("redline.png")
data = list(im.getdata())
s = ""
for i in data :
    s += hex(i[0])[2:]
print s