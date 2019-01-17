from PIL import Image

im = Image.open("rankkix.gif", "r")
width, height = im.size
pix = im.load()
data = list(im.getdata())

for i in range(height) :
	for j in range(width) :
		x = pix[j,i]
		if x != 4 :
			pix[j,i] = 16

im.save("out.gif")