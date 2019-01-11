cipher = "131017171A48221A1D170F"
c = []
temp = cipher
while temp :
	c.append(temp[:2])
	temp = temp[2:]

# 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z
# 02030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F202122232425
# hello world
