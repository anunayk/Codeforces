def primesUpTo(N):
	table = list(range(N))
	for i in range(2,int(N**0.5)+1):
		if table[i]:
			for mult in range(i**2,N,i):
				table[mult] = False
	primes = [p for p in table if p][1:]
	return primes

def getnearest(i, primes):
	if (i == 1):
		return 1
	elif (i == 2) or (i == 3):
		return 0
	j = 0
	m2 = 0
	while (j < len(primes)):
		if (primes[j]<i) and (primes[j+1]>=i):
			m2 = primes[j+1]
			break
		j+=1
	if (j == len(primes)):
		m2 = primes[j-1]
	return (m2-i)

def getsum(s):
	ans = 0
	for e in s:
		ans += e
	return ans
	
primes = primesUpTo(100000)

r = map(int, raw_input().split())
m, n = r[0], r[1]

mat = []

j = 0
for i in range(0, m):
	r = map(int, raw_input().split())
	for j in range(0, n):
		r[j] = getnearest(r[j], primes)
	mat.append(r)

ans = getsum(mat[0])
for e in mat:
	if (ans > getsum(e)):
		ans = getsum(e)

for i in range(0, n):
	k = 0
	for j in range(0, m):
		k += mat[j][i]
	if (ans > k):
		ans = k

print ans