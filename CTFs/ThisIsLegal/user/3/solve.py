from PIL import Image
import os

for i in os.listdir("output/") :
    print i
    im = Image.open("output/%s" % i)
    width, height = im.size
    pix = im.load()

    colours = []
    for x in range(width) :
        if pix[x,0] not in colours :
            colours.append(pix[x,0])
    for y in range(height) :
        if pix[0,y] not in colours :
            colours.append(pix[0,y])
    print colours
    break