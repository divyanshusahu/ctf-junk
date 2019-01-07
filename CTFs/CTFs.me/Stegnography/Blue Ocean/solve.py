from qrtools import QR
from PIL import Image

im = Image.open('im.png', 'r')
pix = im.load()
width, height = im.size

for i in range(height) :
    for j in range(width) :
        r,g,b,a = pix[j,i]
        if r != 255 :
            pix[j,i] = 0,0,0,255

im.save('out.png')

qr = QR(filename = 'out.png')
print qr.decode(), qr.data