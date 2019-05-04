with open("input.txt","rb") as f :
    data = f.readlines()

#print data[0].rstrip()
colors = []

for line in data :
    t = line.rstrip().split("+")
    for p in t :
        c = p.split("x")
        x = [int(c[0])]*int(c[1])
        colors += x

from PIL import Image

img = Image.new("RGB",(100,12), (0,0,0))
pix = img.load()

width, height = img.size

count = 0
for i in range(height) :
    for j in range(width) :
        if colors[count] == 0 :
            pix[j,i] = 255,255,255
        else :
            pix[j,i] = 0,0,0
        count += 1

img.save("out.png","PNG")