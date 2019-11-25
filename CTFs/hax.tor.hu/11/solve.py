from bs4 import BeautifulSoup
import requests
from hashlib import md5

url = "http://hax.tor.hu/level11/"
cookies = {"HAXTOR" : "b4ci8ccsaoi1k99tcglpnu85t1"}

r = requests.get(url, cookies=cookies)
soup = BeautifulSoup(r.text, "lxml")
data = soup.find("td",{"class":"description"}).text
text = data.split(":")[1].split('"')[1]
text = text.replace(" ","")
send = md5(text).hexdigest()

u2 = url + "?pw=" + send
r1 = requests.get(u2, cookies=cookies)
print r1.status_code