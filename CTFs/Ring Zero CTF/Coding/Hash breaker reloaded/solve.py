from bs4 import BeautifulSoup
import requests
import hashlib

cookies = {"PHPSESSID": "1k2ir7liqi97nnnn8341ck5tr3"}
challenge_url = "https://ringzer0ctf.com/challenges/57/"

r = requests.get(challenge_url, cookies=cookies)
soup = BeautifulSoup(r.text, "lxml")
message = soup.find_all("div", {"class": "message"})

hashed = message[0].text.replace('\r\n\t\t', '').replace('\n', '')
start_string = '----- BEGIN HASH -----'
end_string = '----- END HASH -----'
hashed = hashed.replace(start_string, '')
hashed = hashed.replace(end_string, '')

salt = message[1].text.replace('\r\n\t\t', '').replace('\n', '')
salt = salt.replace('----- BEGIN SALT -----', '').replace('----- END SALT -----','')

with open('dict.list', 'rb') as f :
    data = f.readlines()

for num in data :
	cur = num.rstrip() + salt
	h = hashlib.sha1(cur)
	cur_hash = h.hexdigest()
	if cur_hash == hashed :
		answer = num.rstrip()
		r2 = requests.get(challenge_url+answer, cookies=cookies)
		print r2.text
		break