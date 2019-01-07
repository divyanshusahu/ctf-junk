from bs4 import BeautifulSoup
import requests
import hashlib

cookies = {"PHPSESSID": "1k2ir7liqi97nnnn8341ck5tr3"}
challenge_url = "https://ringzer0ctf.com/challenges/56/"

r = requests.get(challenge_url, cookies=cookies)
soup = BeautifulSoup(r.text, "lxml")
message = soup.find("div", {"class": "message"}).text
message = message.replace('\r\n\t\t', '').replace('\n', '')
start_string = '----- BEGIN HASH -----'
end_string = '----- END HASH -----'
message = message.replace(start_string, '')
message = message.replace(end_string, '')

with open('dict.list', 'rb') as f :
    data = f.readlines()

for num in data :
    cur = num.rstrip()
    h = hashlib.sha1(cur)
    cur_hash = h.hexdigest()
    if cur_hash == message :
        answer = cur
        r1 = requests.get(challenge_url+answer, cookies=cookies)
        print r1.text
        print answer
        break
