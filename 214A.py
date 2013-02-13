k = raw_input()
k = k.split()

n = int(k[0])
m = int(k[1])

ans = 0

i = 0
while (i ** 2 <= n):
	j = n - i**2
	if (i + j**2 == m):
		ans += 1
	i += 1
		
print ans