import requests
from PIL import Image
from morse import decrypt
from bs4 import BeautifulSoup

url = "https://www.hackthissite.org/missions/prog/2/index.php"
img_url = "https://www.hackthissite.org/missions/prog/2/PNG/"

cookies = {
    "PHPSESSID": "jfe4h16ojfomhgevte712rass3",
    "phpbb3_28pla_u" : "1",
    "phpbb3_28pla_sid": "c7da34895d87609b69eb45e26e0c4741",
    "phpbb3_28pla_k" : None
}
r0 = requests.get(url, cookies=cookies)
r = requests.get(img_url, cookies=cookies, stream=True)
with open("img.png", "wb") as f :
    for chunk in r :
        f.write(chunk)

im = Image.open("img.png", "r")
width, height = im.size
pix = im.load()
temp = []

for i in range(height) :
    for j in range(width) :
        if pix[j,i] == 1 :
            temp.append(j+width*i)

i = 1
message = chr(temp[0])

while i < len(temp) :
    c = temp[i] - temp[i-1]
    message += chr(c)
    i += 1

text = decrypt(message).replace(" ","")
data = {"solution": text, "submitbutton": "submit"}
headers = {"Referer": "https://www.hackthissite.org/missions/prog/2/"}
r1 = requests.post(url, cookies=cookies, data=data, headers=headers)
soup = BeautifulSoup(r1.text, "lxml")
result = soup.find("td", {"class":"sitebuffer"})
