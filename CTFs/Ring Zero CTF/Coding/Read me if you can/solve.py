from bs4 import BeautifulSoup
import requests
from base64 import b64decode
from PIL import Image
import os
import subprocess

cookies = {"PHPSESSID": "1k2ir7liqi97nnnn8341ck5tr3"}
challenge_url = "https://ringzer0ctf.com/challenges/17/"

r = requests.get(challenge_url, cookies=cookies)
soup = BeautifulSoup(r.text, "lxml")
message = soup.find("div", {"class": "message"})
data = message.find("img")["src"]
data = data[22:]
data = b64decode(data)
with open('chall.png', 'wb') as f :
    f.write(data)


im = Image.open('chall.png', 'r')
pix = im.load()
width, height = im.size

for i in range(height) :
    for j in range(width) :
        r,g,b = pix[j,i]
        if r>240 and b>240 and g > 240:
            pix[j,i] = 255,255,255
        else :
            pix[j,i] = 0,0,0

im.save('resolve.png')

answer = subprocess.check_output("gocr -i resolve.png", shell=True)
answer = answer.rstrip()
print answer, len(answer)
r2 = requests.get(challenge_url+answer, cookies=cookies)
print r2.text