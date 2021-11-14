fibsequence = [1, 2]
sum = 0
while True:
	length = len(fibsequence)
	sum = fibsequence[length-2] + fibsequence[length-1]
	if sum > 4000000:
		break
	fibsequence.append(sum)
evensum = 0
for x in fibsequence:
	if x % 2 == 0: # if even
		evensum += x
print(evensum)
