def isPrime(n) :
	 i=2
	 while(i*i<=n) :
	 	if n%i == 0 :
	 		return 0
	 	i += 1
	 return 1

def digitSum(n) :
	sum = 0
	x = n
	while(x) :
		sum += x%10
		x /= 10
	return sum

def main() :
	n = 1000000
	count = 0
	while(count!=2) :
		n += 1
		if isPrime(n) and isPrime(digitSum(n)) :
			print n
			count += 1


if __name__ == '__main__':
	main()