def base(x,n) :
	# for n < 10
	rem = ""
	while x :
		rem += str(x%n)
		x = x/n
	return rem[::-1]

print base(27416,7)