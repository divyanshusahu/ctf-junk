cipher = "b1 a5 93 a5 e2 a5 f6 a5 c6 a5 b6 a5 11 a5 f3 a5 32 a5"
cipher = cipher.replace("a5","").split("  ")

message = ""
for i in cipher :
    c = int(i,16) ^ int("a5",16)
    message += chr(int(hex(c)[2:][::-1],16))
print message