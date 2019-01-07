from PIL import Image

im = Image.open('Stego15.png', 'r')
pix = im.load()
width, height = im.size

data = list(im.getdata())
pix_dict = {}

for p in data :
    pix_dict[p] = pix_dict.get(p,0) + 1
print width*height, len(data), len(pix_dict)

count1 = 0
count2 = 0
count3 = 0

for i in pix_dict :
    if pix_dict[i] == 1 :
        count1 += 1
    elif pix_dict[i] == 2 :
        count2 += 1
    else :
        count3 += 1

print count1, count2, count3

for i in range(height) :
    for j in range(width) :
        x = pix[j,i]
        if pix_dict[x] == 1 :
            pix[j,i] = 0,0,0
        else :
            pix[j,i] = 255,255,255
im.save('out.png')