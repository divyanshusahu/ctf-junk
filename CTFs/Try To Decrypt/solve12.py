from bs4 import BeautifulSoup
import requests
import string

m = string.lowercase + string.uppercase + string.digits + " -_.,;:?!"

def divide_cipher(s) :
	l = []
	count = 0
	temp = ""
	for i in s :
		temp += i
		count += 1
		if count % 3 == 0 :
			l.append(temp)
			temp = ""
	return l

cipher = divide_cipher("00D02703603C0450461340870A50B50EA10A0BD133")

url = "https://www.trytodecrypt.com/decrypt.php?id=12#headline"
cookies = {"PHPSESSID" : "1712427a8d1a8a693e152abfdf297fa0"}

message = ""
current_cipher = ""

for c in cipher :
	current_cipher += c
	for i in m :
		form_data = {
			"text" : message+i,
			"encrypt" : ""
		}
		r = requests.post(url, cookies=cookies, data=form_data)
		soup = BeautifulSoup(r.text, "lxml")
		encrypted = soup.find_all("div", {"class" : "panel-body"})[1].text

		if encrypted == current_cipher :
			message += i
			print message + "*"*(len(cipher)-len(message))
			break