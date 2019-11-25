password = {}
check = "jU5t_a_sna_3lpm12gb44_u_4_m1r240"

for i in range(0,8) :
    password[i] = check[i]

for i in range(8,16) :
    password[23-i] = check[i]

for i in range(16,32,2) :
    password[46-i] = check[i]

for i in range(31,15,-2) :
    password[i] = check[i]

p = ""
for i in range(32) :
    p += password[i]

print(p)
