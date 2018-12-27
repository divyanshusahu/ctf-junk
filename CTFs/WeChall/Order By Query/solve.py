import requests

# "SELECT * FROM users ORDER BY $orderby $dir LIMIT 10";
# " .... order by 5";
order_by = '5"; %23'
url = "https://www.wechall.net/challenge/order_by_query/index.php?by=%s" % order_by
r = requests.get(url)
print r.text
print url
