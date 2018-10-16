from PIL import Image

im = Image.open('secret.png','r')
pix = im.load()
width,height = im.size

for i in range(width) :
	for j in range(height) :
		r,g,b,o = pix[i,j]
		if b == 254 :
			pix[i,j] = 0,0,0,255

im.save('flag.png')