import string

with open("found1", "rb") as f :
	data1 = f.read()

with open("found2", "rb") as f :
	data2 = f.read()

with open("found3", "rb") as f :
	data3 = f.read()

key1 = {}
for i in data1 :
	key1[i] = key1.get(i,0) + 1

key2 = {}
for i in data2 :
	key2[i] = key2.get(i,0) + 1

key3 = {}
for i in data3 :
	key3[i] = key3.get(i,0) + 1

key = {}
key[" "] = key1[" "] + key2[" "] + key3[" "]

for i in string.ascii_uppercase :
	key[i] = key1.get(i,0) + key2.get(i,0) + key3.get(i,0)

temp = sorted(key.values(), reverse=True)

letter_freq = " etaoinshrdlcumwfgypbvkjxqz".upper()
subs = {}
for i,j in enumerate(temp) :
	#print i,j, key.keys()[key.values().index(j)]
	subs[key.keys()[key.values().index(j)]] = letter_freq[i]
	del key[key.keys()[key.values().index(j)]]

with open("krypton4", "rb") as f :
	cipher = f.read()

message = ""
for l in data1 :
	message += subs[l]
print message