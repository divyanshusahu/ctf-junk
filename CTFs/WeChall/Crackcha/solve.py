import requests
from PIL import Image
from pytesseract import image_to_string

cookies = {"WC": "11098479-37667-ATTdbCcWQrloi9m8"}
challenge_url = "https://www.wechall.net/challenge/crackcha/"
reset_url = challenge_url + "reset.php"
problem_url = challenge_url + "problem.php"
answer_url = challenge_url + "answer.php"

r = requests.get(reset_url, cookies=cookies)
for i in range(1) :
    r = requests.get(problem_url, cookies=cookies, stream=True)
    if r.status_code == 200 :
        with open('captcha.jpeg', 'wb') as f :
            for chunk in r :
                f.write(chunk)
    #ans = image_to_string(Image.open('captcha.jpeg'), lang='eng')
    #print ans
