# Fibonacci sequence

def feb(n) :
	if n == 1 or n == 2 :
		return 1

	a, b = 1, 1
	count = 2
	while True :
		cur = a + b
		count += 1
		if count == n :
			return cur
			break
		a = b
		b = cur

print feb(78)