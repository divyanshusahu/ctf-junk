with open("lorem.txt", "rb") as f :
    data = f.read().replace("\n"," ").replace("\r"," ")

k = {}
data = data.split(" ")
for i in data :
    k[i] = k.get(i,0) + 1

keys = k.keys()
for i in keys :
    if k[i] == 1 :
        print i, k[i]