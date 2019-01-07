import requests

cookies = {
    "PHPSESSID": "g5b4st9oicasno5duif0a9ebj3",
    "member": "1",
    "autologin": "%ADG%A3%8AO%A5%97%5EC%B3Dr%A8%9Fp%E7%3C%A1%C9%CC%D8%2B%3CU%C0%E3%08m%A2%FB%AE%1D%2Ct%E2%A0%A8%B5%AF%1C%19w%CD%E4WT%88%12b%9D%19%5C%FF%D4%B7%2A%A7t%23%0A%2C9P%DD"
}

challange_url = "https://www.hackthis.co.uk/levels/b3.php?submit"
data = {"score": "194175"}
r = requests.post(challange_url, cookies=cookies, data=data)
print r.text