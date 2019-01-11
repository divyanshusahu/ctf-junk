import requests
from pytesseract import image_to_string
from PIL import Image

cookies = {"ci_session": "b8217111567c26da41946d4941c14609b893e2f8"}
url = "http://challengeland.co/Challenges/Captcha/d6c19a9b72"

r1 = requests.get(url, cookies=cookies)
r = requests.get(url+"Captcha", cookies=cookies, stream=True)
with open("im.png", "wb") as f :
    for chunk in r :
        f.write(chunk)

answer = image_to_string(Image.open("im.png"), lang="eng")
print answer[:6]
data = {"solve":answer[:6]}
r2 = requests.post(url+"Solve", cookies=cookies, data=data)
print r2.text
