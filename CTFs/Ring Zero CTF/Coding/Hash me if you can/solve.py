import requests
from bs4 import BeautifulSoup
import hashlib

cookies = {"PHPSESSID": "3tg4a9an9tk1p3gbmh6rkir2p0"}
challange_url = "https://ringzer0ctf.com/challenges/13/"

r = requests.get(challange_url, cookies=cookies)
soup = BeautifulSoup(r.text, "lxml")
message = soup.find("div", {"class": "message"}).text
message = message.replace('\r\n\t\t', '').replace('\n', '')
start_string = '----- BEGIN MESSAGE -----'
end_string = '----- END MESSAGE -----'
message = message.replace(start_string, '')
message = message.replace(end_string, '')

h = hashlib.sha512(message)
answer = h.hexdigest()
r2 = requests.get(challange_url+answer, cookies=cookies)
print r2.text