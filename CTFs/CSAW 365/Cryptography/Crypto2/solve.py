with open('data.txt', 'rb') as f:
    cipher = f.read().split(':')

message = ''
for i in cipher:
    message += chr(int(i, 16))
print message