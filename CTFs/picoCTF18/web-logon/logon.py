import requests

data = {'user':'admi', 'password':'an'}
url = 'http://2018shell1.picoctf.com:5477/login'
#cookies = {'admin':'True','password':'a','user':'a'}

s = requests.Session()
r = s.post(url, data=data)
print(r.status_code)
print(r.request.headers)
print(r.url)