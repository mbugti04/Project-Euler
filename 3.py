def is_prime_factor(num):
	factors = []
	for x in range(1, int(num ** 0.5)):
		if num % x == 0:
			factors.append(x)
			factors.append(num//x)
	# print(num, factors)
	return len(factors) < 3
		
	
numtofactor = 600851475143

factors = []
prime_factors = []
for x in range(1, int(numtofactor ** 0.5)):
		if numtofactor % x == 0:
			factors.append(x)
			factors.append(numtofactor//x)

			if is_prime_factor(x):
				prime_factors.append(x)
			if is_prime_factor(numtofactor//x):
				prime_factors.append(numtofactor//x)

factors.sort()
prime_factors.sort()

# print(factors)
# print(prime_factors)
largest_prime_factor = prime_factors[len(prime_factors)-1]
print(largest_prime_factor)