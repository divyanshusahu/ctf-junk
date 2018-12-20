from PIL import Image

im = Image.open('sorted.png', 'r')
pix = im.load()
width, height = im.size

colors = list(im.getdata())
im2 = Image.open('b.png', 'r')
colors2 = list(im2.getdata())

new_img = []

for i,j in zip(colors, colors2) :
	temp = ()
	for x,y in zip(i,j) :
		temp += ((x^y)%256,)
	temp_list = list(temp)
	temp_list.pop(3)
	temp_list.append(255)
	temp = tuple(temp_list)
	new_img.append(temp)

index = 0
for l in range(height) :
	for m in range(width) :
		pix[m,l] = new_img[index]
		index += 1

im.save('xor.png')