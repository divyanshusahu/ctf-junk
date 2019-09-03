from bs4 import BeautifulSoup
import string
import requests
import sys

CIPHER = "3785824AD56B2531A7150DF44C21434A61E63F040A42F2012BC2F43F0AD535D24D46013213866D7E0"
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

cipher = divide_cipher(CIPHER)

# Attack idea
"""
url = "https://www.trytodecrypt.com/decrypt.php?id=11#headline"
cookies = {"PHPSESSID" : "1712427a8d1a8a693e152abfdf297fa0"}
form_data = {
	"text" : string.lowercase,
	"encrypt" : ""
}
r = requests.post(url, cookies=cookies, data=form_data)
soup = BeautifulSoup(r.text, "lxml")
print soup.find_all("div", {"class":"panel-body"})[1]
"""

url = "https://www.trytodecrypt.com/decrypt.php?id=11#headline"
cookies = {"PHPSESSID" : "1712427a8d1a8a693e152abfdf297fa0"}

"""for i in string.uppercase :
	form_data = {
	"text" : i+i,
	"encrypt" : ""
	}
	r = requests.post(url, cookies=cookies, data=form_data)
	soup = BeautifulSoup(r.text, "lxml")
	c = soup.find_all("div", {"class" : "panel-body"})[1].text
	print i+i,c"""

"""					difference between every first alphabet is 12
a 120				difference between every second alphabet is 47
b 12C				
c 138
d 144
e 150
f 15C
g 168
h 174
i 180
j 18C
k 198
l 1A4
m 1B0
n 1BC
o 1C8
p 1D4
q 1E0
r 1EC
s 1F8
t 204
u 210
v 21C
w 228
x 234
y 240
z 24C
"""

# Pure bruteforce attack

message = "You are "
current_cipher = "3785824AD56B2531A7150DF4"

for c in cipher[8:] :
	current_cipher += c
	for i in m :
		#print i
		form_data = {
			"text" : message+i,
			"encrypt" : ""
		}
		r = requests.post(url, cookies=cookies, data=form_data)
		soup = BeautifulSoup(r.text, "lxml")
		encrypted = soup.find_all("div", {"class" : "panel-body"})[1].text

		#print(i, end="\r")
		
		if encrypted == current_cipher :
			message += i
			print(message)
			break