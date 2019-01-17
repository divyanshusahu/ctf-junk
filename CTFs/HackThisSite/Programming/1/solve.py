import requests
from itertools import permutations
from bs4 import BeautifulSoup

with open("wordlist.txt", "rb") as f :
    data = f.readlines()

url = "https://www.hackthissite.org/missions/prog/1/"
cookies = {"PHPSESSID": "209h4fef2knp5q46hjic31oe13"}
r = requests.get(url, cookies=cookies)
soup = BeautifulSoup(r.text, "lxml")
tables = soup.find_all("table")
list_words = tables[3].find_all("li")
words = []
for i in list_words :
    words.append(str(i.text))

def unscamble(word, wl) :
    perm = list(permutations(word))
    perms = []
    for i in perm :
        temp = ''
        for j in i :
            temp += j
        perms.append(temp)
    solutions = []
    for w in wl :
        cur = w.rstrip()
        if cur in perms :
            solutions.append(cur)
    return solutions

solutions = []
for w in words :
    solutions.append(unscamble(w, data))
answer = ""
for i in solutions :
    answer += i[0]+","
answer = answer[:-1]

headers = {"Referer": "https://www.hackthissite.org/missions/prog/1/"}
r1 = requests.post(url+"index.php", cookies=cookies, data={"solution":answer, "submitbutton":"submit"}, headers=headers)
soup1 = BeautifulSoup(r1.text, "lxml")
result = soup1.find("td", {"class": "sitebuffer"})
print result
