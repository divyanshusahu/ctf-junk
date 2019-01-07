import requests
from bs4 import BeautifulSoup

cookies = {"PHPSESSID": "3tg4a9an9tk1p3gbmh6rkir2p0"}
challenge_url = "https://ringzer0ctf.com/challenges/32/"

r = requests.get(challenge_url, cookies=cookies)
soup = BeautifulSoup(r.text, "lxml")
message = soup.find("div",{"class":"message"}).text
message = message.replace('\r\n\t\t', '').replace('\n','')
start_string = '----- BEGIN MESSAGE -----'
end_string = ' = ?----- END MESSAGE -----'
message = message.replace(start_string, '')
message = message.replace(end_string, '')
question = message.split('-')
answer = eval(str(question[0])) - int(str(question[1]), 2)
r2 = requests.get(challenge_url+str(answer), cookies=cookies)
print r2.text