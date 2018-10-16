#!/usr/bin/python3

import requests

url = 'http://2018shell1.picoctf.com:46162/flag'
r = requests.get(url, headers={'User-Agent':'Googlebot'})
print(r.url)
print(r.headers)
print(r.request.headers)
print(r.cookies)
print(r.text)