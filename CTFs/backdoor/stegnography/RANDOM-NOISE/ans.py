from PIL import Image

im = Image.open('b.png','r')
pix = im.load()
width, height = im.size

data = list(im.getdata())
out_image = []

hist = {}
for p in data :
	hist[p] = hist.get(p,0) + 1
#print hist
count1, count4159 = 0, 0

for p in data :
	if hist[p] == 4159 :
		count4159 += 1
		out_image.append(0)
	else :
		out_image.append(255)
		count1 += 1

#print out_image

index = 0
for i in range(height) :
	for j in range(width) :
		pix[j,i] = out_image[index]
		index += 1

im.save('boom.bmp')

# Result into morse 
# morse decode YSIYSWFGYLHVNAMXKSZHWUMG
# Decode vigenere ciphere with key THISKEYCANTBEGUESSED is FLAGISHEYYOUJUSTSAVEDNEO