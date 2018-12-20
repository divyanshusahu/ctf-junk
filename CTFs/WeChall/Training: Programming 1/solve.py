#!/usr/bin/python2

import requests

visiting_url = "https://www.wechall.net/challenge/training/programming1/index.php?action=request"
cookies = {"WC":"11068160-37667-z1PuydshfLuLpXFI"}
answer_url = "https://www.wechall.net/challenge/training/programming1/index.php?answer="
r = requests.get(visiting_url, cookies=cookies)
message = r.text
print message
answer_url += message
r2 = requests.get(answer_url, cookies=cookies)
print r2.text
