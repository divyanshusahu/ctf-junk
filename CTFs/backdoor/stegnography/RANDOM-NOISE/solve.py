from PIL import Image

im = Image.open('b.png', 'r')
pix = im.load()
width, height = im.size
colors = []
x = sorted(list(im.getdata()))

index = 0
for i in range(height) :
	for j in range(width) :
		pix[j,i] = x[index]
		index += 1

im.save('sorted.png')