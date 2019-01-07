#import urllib
import requests
from PIL import Image
from pytesseract import image_to_string

cookies = {"WC": "11098479-37667-ATTdbCcWQrloi9m8"}

image_url = "https://www.wechall.net/challenge/can_you_readme/gimme.php"
#urllib.urlretrieve(image_url, "ocr.png")
r = requests.get(image_url, stream=True, cookies=cookies)
if r.status_code == 200 :
    with open('ocr.png', 'wb') as f :
        for chunk in r :
            f.write(chunk)

answer = image_to_string(Image.open('ocr.png'), lang='eng')
challenge_url = "https://www.wechall.net/challenge/can_you_readme/index.php?solution=%s&cmd=Answer" % answer
r = requests.get(challenge_url, cookies=cookies)
print r.text