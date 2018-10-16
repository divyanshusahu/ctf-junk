from PIL import Image

def fillLength(string) :
	if len(string) < 8 :
		string = "0"*(8-len(string)) + string
	return string

flag = "CTF{you_are_learning_quickly!}"

binary = ''

for i in flag:
	char = bin(ord(i))[2:]
	char = fillLength(char)
	binary += char

#print len(binary)
pixels = []

im = Image.open('hidden.png','r')
width, height = im.size
pix = im.load()

for i in range(height) :
	for j in range(width) :
		r,g,b = pix[j,i]
		pixels.append(r)
		pixels.append(g)
		pixels.append(b)

new_pixels = []

for i,j in zip(pixels,binary) :
	i = bin(i)[2:]
	i = i[:7]+j
	i = int(i,2)
	new_pixels.append(i)

#print new_pixels

flag_pixels = []

for j in range(0,len(new_pixels),3) :
	flag_pixels += [[new_pixels[j],new_pixels[j+1],new_pixels[j+2]]]
#print len(flag_pixels)

count = 0
for i in range(height) :
	for j in range(width) :
		r,g,b = flag_pixels[count]
		#print r,g,b
		pix[j,i] = r,g,b
		print pix[j,i]
		count += 1

im.save('secret.png')