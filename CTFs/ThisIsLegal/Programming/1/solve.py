import requests

cookies = {"PHPSESSID": "cio9psl54ibs86mphns9c4tbr7"}
url = "https://thisislegal.com/includes/randCode.php"
r = requests.get(url, cookies=cookies)
data = r.text.split(":")
code = data[1][1:10]
submit_url = "https://thisislegal.com/challenge/programming/1/%s" % code
r2 = requests.get(submit_url, cookies=cookies)
print r2.text