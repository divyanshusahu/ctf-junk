import string

message_chars = string.letters + string.digits + "-_.,;:?! "
solves = "270B41450E1011052F1C161804353E371D1F15211A23000C3B301E13253C292C31220D0F34383A3D02082D362432200A063F"
solves += "19142A1B43172B012E093339402603420744284612"
cipher = "21052F151200271512413E35101A152F3511"

key = {}
index = 0
s = solves
while s:
    key[s[:2]] = message_chars[index]
    index += 1
    s = s[2:]

c = cipher
m = ""
while c:
    m += key[c[:2]]
    c = c[2:]
print m
