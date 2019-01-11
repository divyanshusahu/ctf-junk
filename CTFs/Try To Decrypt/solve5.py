import string

cipher = "90DE633F425148DE51546CDE725466DE3F2A6936DE4263CCDEAB362A3372DE39545DDE633F36DE51366F63DE545136D8"
message_chars = string.letters + string.digits + "-_.,;:?! "
solves = "2A2D303336393C3F4245484B4E5154575A5D606366696C6F7275787B7E8184878A8D909396999C9FA2A5A8ABAEB1B4B7BABDC0C30C0F1215181B1E212427C6C9CCCFD2D5D8DBDE"

key = {}
index = 0
s = solves
while s :
    key[s[:2]] = message_chars[index]
    index += 1
    s = s[2:]

c = cipher
m = ""
while c :
    m += key[c[:2]]
    c = c[2:]
print m
