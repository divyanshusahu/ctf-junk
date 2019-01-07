from PIL import Image

def resolve(s) :
    im = Image.open(s,'r')
    pix = im.load()
    width, height = im.size
    data = list(im.getdata())
    pix_dict = {}

    for p in data :
        pix_dict[p] = pix_dict.get(p,0) + 1
    #print width, height, len(pix_dict)
    #print pix_dict

    index = 0
    for i in range(height) :
        for j in range(width) :
            freq = pix_dict[data[index]]
            if freq <= 9 and i>10 and i < 32:
                pix[j,i] = 255,0,0
            else :
                pix[j,i] = 255,255,255
            index += 1
            
    im.save('out.jpeg')

resolve('captcha.jpeg')