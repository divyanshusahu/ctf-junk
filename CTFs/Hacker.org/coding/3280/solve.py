with open("rfc3280.txt", "rb") as f :
    data = f.read().replace("\n","")

t = data.split(" ")
k = {}
for i in t :
    k[i] = k.get(i,0) + 1
val = sorted(k.values(), reverse=True)

for i in k :
    if len(i) == 9 or len(i) == 10 :
        print i, k[i]