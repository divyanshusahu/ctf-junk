#!/usr/bin/python3

import requests

"""url1 = 'http://2018shell1.picoctf.com:44730/button1.php'
r = requests.post(url1)
print(r.url)
print(r.headers)
print(r.request.headers)
print(r.cookies)"""

url2 = 'http://2018shell1.picoctf.com:44730/button2.php'
r = requests.post(url2)
print(r.url)
print(r.headers)
print(r.request.headers)
print(r.cookies)
print(r.text)