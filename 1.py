multiples = []
for x in range(0, 1000):
	if x % 3 == 0 or x % 5 == 0:
		multiples.append(x)
sum = 0
for x in multiples:
	sum += x
print(sum)