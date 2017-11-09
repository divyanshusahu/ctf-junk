from PIL import Image

f = open('flag.zip','r')
content = f.read()

def fillLength(string) :
	if len(string) < 8 :
		string = "0"*(8-len(string)) + string
	return string

binary = ''
for s in content :
	char = bin(ord(s))[2:]
	char = fillLength(char)
	binary += char
#print binary

pixels = []

im = Image.open('hidden.png','r')
width,height = im.size
pix = im.load()

for i in range(height) :
	for j in range(width) :
		r,g,b = pix[j,i]
		pixels.append(r)
		pixels.append(g)
		pixels.append(b)
#print pixels

new_pixels = []
count1 = 0
for i,j in zip(pixels,binary) :
	i = bin(i)[2:]
	i = i[:7]+j
	i = int(i,2)
	new_pixels.append(i)
	count1 += 1
	if count1 == len(binary) :
		new_pixels.append(255)
		new_pixels.append(255)
		break
#print new_pixels

flag_pixels = []

for j in range(0,len(new_pixels),3) :
	flag_pixels += [[new_pixels[j],new_pixels[j+1],new_pixels[j+2]]]
#print flag_pixels

count = 0
for i in range(height) :
	for j in range(width) :
		r,g,b = flag_pixels[count]
		#print r,g,b
		pix[j,i] = r,g,b
		print pix[j,i]
		count += 1

#im.save('secret.png')

f = open('hidden.png','r')
data = f.read()
f.close()

string = "Password is: babyboss"
string = string[::-1]
print string

f = open('hidden.png','a')
f.write(password)
f.close()