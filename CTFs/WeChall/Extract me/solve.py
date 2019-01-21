with open("r.zip", "rb") as f :
    data = f.read()

data1 = data[:440]
data2 = data[440:]

with open("t1.zip", "wb") as f :
    f.write(data1)

with open("out", "wb") as f :
    f.write(data2)