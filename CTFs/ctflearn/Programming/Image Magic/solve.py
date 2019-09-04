from PIL import Image

im = Image.open("out.jpg","r")
data = list(im.getdata())
width, height = im.size

new_width, new_hight = 92, width/92
new_img = Image.new(im.mode, (new_width, new_hight))
new_img.putdata(data)
new_img.save("recover.jpg")