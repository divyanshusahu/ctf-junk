from PIL import Image

im = Image.open("index.png")
data = list(im.getdata())
#print data

pix = im.load()
width, height = im.size

for i in range(height) :
	for j in range(width) :
		if pix[j,i] == (6,6,6,255) :
			pix[j,i] = 255,255,255,255

im.save("out.png")