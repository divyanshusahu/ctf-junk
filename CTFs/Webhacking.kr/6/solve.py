from base64 import b64encode

user = "admin"
password = "admin"

for i in range(20) :
    user = b64encode(user)
    password = b64encode(password)

user = user.replace("1", "!").replace("2", "@").replace("3", "$").replace("4","^")
user = user.replace("5", "&").replace("2", "*").replace("3", "(").replace("4",")")

password = password.replace("1", "!").replace("2", "@").replace("3", "$").replace("4", "^")
password = password.replace("5", "&").replace("6", "*").replace("7", "(").replace("8", ")")

print user
print password