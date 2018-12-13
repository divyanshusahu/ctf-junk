with open('data.txt', 'rb') as f:
    cipher = f.read()

message = ''
s = cipher
while(s) :
    cur = s[:8]
    message += chr(int(cur,2))
    s = s[8:]
print message