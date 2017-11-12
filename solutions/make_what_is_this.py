from PIL import Image
from random import *

im = Image.open('anin.jpg','r')
width,height = im.size
pix = im.load()

pixels = []
oldpixels = []
for j in range(height) :
	for i in range(width) :
		r,g,b = pix[i,j]
		pixels.append(r)
		pixels.append(g)
		pixels.append(b)
		oldpixels.append(r)
		oldpixels.append(g)
		oldpixels.append(b)
		#print r,g,b

#print pixels

def fillLength(string) :
	if len(string) < 8 :
		string = "0"*(8-len(string)) + string
	return string

flag = "CTF{FUCK_OFF!}"
binary = ''
for i in flag:
	j = bin(ord(i))[2:]
	j = fillLength(j)
	binary += j
#print len(binary)

	#print n
	#if new_pixels[n] != oldpixels[n] :	
	#	print n,pixels[n], oldpixels[n]
	
	
	
#for i,j in zip(oldpixels,new_pixels) :
#	if i != j :
#		print 'yo'
#print new_pixels
#print pixels[20]
count = 20
#check =1

for i in binary :
	check = 1
	while check == 1 :
		#print i == str(0) ,pixels[count]%2 == 1
		if i == str(0) and pixels[count]%2 == 1 :
		 	pixels[count] = pixels[count] + 1
		 	if pixels[count] == 256:
				pixels[count] = 254
			#print 'done1'
			check = 0
		if int(i) == 1 and pixels[count]%2 == 0 :
			pixels[count] = pixels[count] + 1
		 	if pixels[count] == 256:
				pixels[count] = 254
			check = 0
			#print 'done2'
		count += 20
	#print i

#for i in range(len(pixels)) :
#	if pixels[i] != oldpixels[i] :
#		print 'yo'

print pixels