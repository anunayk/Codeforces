r = raw_input('')
numer = raw_input('')
denom = raw_input('')

numer = numer.split()
numer = map(int, numer)
denom = denom.split()
denom = map(int, denom)

m = len(numer)
n = len(denom)

numerator = 1
denominator = 1

def gcd(a,b):
	while a:
		a, b = b%a, a
	return b

i = 0
while (i < n):
	j = 0
	while (j < m):
		g = gcd(numer[j], denom[i])
		numer[j] /= g
		denom[i] /= g
		j += 1
	i += 1

print len(numer), len(denom)
numer = map(str, numer)
print ' '.join(numer)
denom = map(str, denom)
print ' '.join(denom)