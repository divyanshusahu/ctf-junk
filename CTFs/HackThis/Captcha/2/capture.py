import requests
from PIL import Image

cookies = {
    "autologin": "%16%DC%7B%D2%07%B8%3A%11%BA%26%95%A6%A5%18o%2B%AE-x%AC%F0%F5%E42%C7S%AD%CAY%E3aPt%B0%12%F8%B3%C4%8F%5B%86%F5%B0F%83%D8%80%D4T%C4%7C%DD%16%D8%06%B7%21w%8FNU%BD%7E%EF",
    "member": "1",
    "PHPSESSID": "79rj6cs0h9b8f25cmi4ii1es94"
}

image_url = "https://www.hackthis.co.uk/levels/extras/captcha2.php"

for i in range(1,101) :
    r = requests.get(image_url, cookies=cookies, stream=True)
    filename = "images/%s.png" % str(i)
    with open(filename, 'wb') as f:
        for chunk in r:
            f.write(chunk)
    
    im = Image.open(filename, 'r')
    im = im.resize((1000,100), Image.ANTIALIAS)
    im.save(filename)