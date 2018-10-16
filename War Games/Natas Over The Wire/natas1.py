import requests

target = 'http://natas1:gtVrDuiDfck831PqWsLEZy5gyDz1clto@natas1.natas.labs.overthewire.org'

r = requests.get(target)
if r.status_code != requests.codes.ok :
	print 'Unable to Connect'
else :
	print 'Connected'
	
print r.content