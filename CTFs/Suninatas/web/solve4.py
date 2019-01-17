import requests

url = "http://suninatas.com/Part_one/web04/web04_ck.asp"
headers = {
    "User-Agent": "SuNiNaTaS",
    "Referer": "http://suninatas.com/Part_one/web04/web04.asp"
}
cookies = {
    "ASPSESSIONIDQACTTCTT": "LMFACLOCGKFDMFDDNNBDIHNF"
}

for i in range(18) :
    r = requests.post(url, cookies=cookies, headers=headers)
    print i