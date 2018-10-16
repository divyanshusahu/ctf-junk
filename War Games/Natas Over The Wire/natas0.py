import requests

target = 'http://natas0:natas0@natas0.natas.labs.overthewire.org'

r = requests.get(target)
if r.status_code != requests.codes.ok :
	print 'Unable to Connect'
else :
	print 'Connected'
	
print r.content