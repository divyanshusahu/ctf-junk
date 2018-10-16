import requests,base64

target = 'http://natas8:DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe@natas8.natas.labs.overthewire.org'

encodedSecret = '3d3d516343746d4d6d6c315669563362'
decodedData = base64.b64decode(encodedSecret.decode('hex')[::-1])

payload = {'secret':decodedData,'submit':'Submit'}
r = requests.post(target,data=payload)

if r.status_code != requests.codes.ok :
	print 'Unable to connect'
else :
	print 'Connected'

print r.text