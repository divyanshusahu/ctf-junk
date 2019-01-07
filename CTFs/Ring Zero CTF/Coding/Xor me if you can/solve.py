from bs4 import BeautifulSoup
import requests
from base64 import b64decode

def xor(s,k) :
	msg =''
	for i in range(len(s)) :
		msg += chr( ord(s[i]) ^ ord(k[i%len(k)]) )
	return msg

cookies = {"PHPSESSID": "1k2ir7liqi97nnnn8341ck5tr3"}
challenge_url = "https://ringzer0ctf.com/challenges/16/"

r = requests.get(challenge_url, cookies=cookies)
soup = BeautifulSoup(r.text, "lxml")
message = soup.find_all("div", {"class": "message"})

xor_key = message[0].text
xor_key = xor_key.replace("\r\n\t\t","").replace("\n","")
xor_key = xor_key.replace("----- BEGIN XOR KEY -----","")
xor_key = xor_key.replace("----- END XOR KEY -----","")

cipher = message[1].text
cipher = cipher.replace("\r\n\t\t","").replace("\n","")
cipher = cipher.replace("----- BEGIN CRYPTED MESSAGE -----","")
cipher = cipher.replace("----- END CRYPTED MESSAGE -----","")
cipher = b64decode(cipher)

keys = []
index = 0
k = xor_key
while(len(k)>=10) :
	cur = k[:10]
	keys.append(cur)
	k = k[1:]

for k in keys :
	m = xor(cipher, k)
	if m.isalnum() :
		answer = m
		break

r2 = requests.get(challenge_url+answer, cookies=cookies)
print r2.text