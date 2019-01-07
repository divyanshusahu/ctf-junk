import requests
from bs4 import BeautifulSoup

cookies = {"PHPSESSID": "be2qt1hmj7dh5ehrejvnbn5664"}
challenge_url = "https://ringzer0ctf.com/challenges/119/"

r = requests.get(challenge_url, cookies=cookies)
soup = BeautifulSoup(r.text, "lxml")
message = soup.find("div",{"class":"message"})
data = str(message)
data = data.replace('<div class="message">\r\n\t\t----- BEGIN MESSAGE -----<br/>\n','')
print data.split('<br/>')
#JSON required to ascii