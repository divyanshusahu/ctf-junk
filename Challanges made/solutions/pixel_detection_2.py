from PIL import Image

im = Image.open('secret.png','r')
width,height = im.size
pix = im.load()

binary = ''

for i in range(height) :
	for j in range(width) :
		r,g,b = pix[j,i]
		binary += bin(r)[len(bin(r))-1] + bin(g)[len(bin(g))-1] + bin(b)[len(bin(b))-1]

flag = ''
p = binary
for s in range(len(binary)/8):
	char = p[:8]
	flag += chr(int(char,2))
	p = p[8:]

print flag