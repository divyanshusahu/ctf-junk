cipher = "131017171A48221A1D170F"
c = []
temp = cipher
while temp :
	c.append(temp[:2])
	temp = temp[2:]

msg = ''