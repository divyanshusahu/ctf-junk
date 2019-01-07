import requests
from bs4 import BeautifulSoup

cookies = {
    "autologin": "J0i%C5w%9BU%7C%99%D3R+c%CD%0FzY%83%AA%29%F2%F7%D4%1B%DE%98s%EF%91%12%CE%16%D7%B6%AE%96%BC%10%15n%05%AD%98%E7%A5%DB%C1%C1.%1B%C5%A4%E5f%23%5E%E8%AA%CD%E2%AEpSj",
    "member": "1",
    "PHPSESSID": "uj2kdhas411kvli50dj8q04uk7"
}

challenge_url = "https://www.hackthis.co.uk/levels/coding/2"

r = requests.get(challenge_url, cookies=cookies)
soup = BeautifulSoup(r.text, "lxml")
cipher = soup.find_all("textarea")[0].text
cipher = cipher.split(',')
total_visible_ascii = 94
decoded_message = ''
for i in cipher :
    if i == ' ' :
        decoded_message += i
        continue
    cur = int(i)
    x = cur - 32
    y = total_visible_ascii - x
    decoded_message += chr(y+32)

r2 = requests.post(challenge_url, cookies=cookies, data={"answer":decoded_message})
print r2.text