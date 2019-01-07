import requests
import subprocess
from PIL import Image
from pytesseract import image_to_string

cookies = {
    "autologin": "%16%DC%7B%D2%07%B8%3A%11%BA%26%95%A6%A5%18o%2B%AE-x%AC%F0%F5%E42%C7S%AD%CAY%E3aPt%B0%12%F8%B3%C4%8F%5B%86%F5%B0F%83%D8%80%D4T%C4%7C%DD%16%D8%06%B7%21w%8FNU%BD%7E%EF",
    "member":"1",
    "PHPSESSID": "79rj6cs0h9b8f25cmi4ii1es94"
}

challenge_url = "https://www.hackthis.co.uk/levels/captcha/1"
image_url = "https://www.hackthis.co.uk/levels/extras/captcha1.php"

r = requests.get(image_url, cookies=cookies, stream=True)
with open('captcha.png', 'wb') as f :
    for chunk in r :
        f.write(chunk)

im = Image.open('captcha.png','r')
pix = im.load()
width, height = im.size

im = im.resize((int(width*10), int(height*10)), Image.ANTIALIAS)
im.save('resolve.png')
print im.size

answer_gocr = subprocess.check_output("gocr -i captcha.png", shell=True)
answer_gocr = answer_gocr.replace('\n','').replace(' ','').replace('6','&').replace('^','*')
answer_tesseract = image_to_string(Image.open('resolve.png')).replace(' ','')
index = answer_gocr.find('_')
answer_gocr = answer_gocr.replace('_', answer_tesseract[index])
index1 = answer_gocr.find('K')
if answer_tesseract[index1] == 'X' :
    answer_gocr = answer_gocr.replace('K','X')
index2 = answer_gocr.find('5')
if answer_tesseract[index2] == 'S' :
    answer_gocr = answer_gocr.replace('5','S')
index3 = answer_gocr.find('?')
if answer_tesseract[index3] != '?' :
    answer_gocr = answer_gocr.replace('?', answer_tesseract[index3])
answer = answer_gocr

data = {"answer":answer[::-1]}
if len(answer) == 40 :
    r2 = requests.post(challenge_url, cookies=cookies, data=data)
    print r2.text
print answer_gocr, len(answer_gocr)
print answer_tesseract, len(answer_tesseract)
print answer, len(answer)
