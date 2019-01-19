from PIL import Image

im = Image.open("blue.png")
data = list(im.getdata())
width, height = im.size

m = ''
for i in data :
    m += chr(i[2])
print m