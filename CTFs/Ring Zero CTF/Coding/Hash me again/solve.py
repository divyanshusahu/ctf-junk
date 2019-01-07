import requests
from bs4 import BeautifulSoup
import hashlib

def bin_to_ascii(s) :
    c = s
    msg = ''
    while(c) :
        cur = c[:8]
        msg += chr(int(cur, 2))
        c = c[8:]
    return msg

cookies = {"PHPSESSID": "3tg4a9an9tk1p3gbmh6rkir2p0"}
challange_url = "https://ringzer0ctf.com/challenges/14/"

r = requests.get(challange_url, cookies=cookies)
soup = BeautifulSoup(r.text, "lxml")
message = soup.find("div", {"class": "message"}).text
message = message.replace('\r\n\t\t', '').replace('\n', '')
start_string = '----- BEGIN MESSAGE -----'
end_string = '----- END MESSAGE -----'
message = message.replace(start_string, '')
message = message.replace(end_string, '')
m = bin_to_ascii(message)

h = hashlib.sha512(m)
answer = h.hexdigest()
r2 = requests.get(challange_url+answer, cookies=cookies)
print r2.text
