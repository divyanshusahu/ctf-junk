from PIL import Image

def fill(s) :
    return "0"*(8-len(s))+s

im = Image.open("didactrgb.png")
data = list(im.getdata())
s = ""
for i in data[0] :
    s += fill(bin(i)[2:])
print s, int(s,2)