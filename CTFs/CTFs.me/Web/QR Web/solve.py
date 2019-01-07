from bs4 import BeautifulSoup
import requests
from qrtools import QR

url = "http://chall.ctfs.me:8002/qrweb/"
r = requests.get(url)
session_cookie = r.cookies['PHPSESSID']
cookies = {"PHPSESSID":session_cookie}
submit_url = url + "validate.php"
print r.headers

for i in range(1,3) :
    print "Stage %s" % str(i)
    soup = BeautifulSoup(r.text, "lxml")
    img = soup.find_all('img')
    image_url = url + img[0]['src']
    r1 = requests.get(image_url, cookies=cookies, stream=True)
    print r1.headers
    if r1.status_code == 200 :
        with open('%s.png'%str(i), 'wb') as f :
            for chunk in r1 :
                f.write(chunk)
    qr = QR(filename = "%s.png"%str(i))
    if qr.decode() :
        answer = qr.data
    data = {"qr":answer, "submit":"Submit+Query"}
    r2 = requests.post(submit_url, cookies=cookies, data=data)
    print r2.headers
    print r2.text
