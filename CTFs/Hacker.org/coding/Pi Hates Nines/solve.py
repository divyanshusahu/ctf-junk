with open("pi1000000.txt", "rb") as f :
    data = f.read()

temp = data.split("9")
max_length = 0
series = ""
for i in temp :
    if len(i) > max_length :
        max_length = len(i)
        series = i
print max_length, series