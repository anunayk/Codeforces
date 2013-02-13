def gcd(a,b):
        """ the euclidean algorithm """
        while a:
                a, b = b%a, a
        return b

k = raw_input()
k = k.split()
n = int(k[0])
m = int(k[1])

k = raw_input()
k = k.split()
j = raw_input()
j = j.split()
x1 = int(k[0])
x2 = int(j[0])

if (n > m):
	ans = 'Infinity'
elif (n < m):
	ans = '0/1'
else:
	g = gcd(x1, x2)
	x1 /= g
	x2 /= g
	ans = str(abs(x1)) + '/' + str(abs(x2))

if x1/x2 < 0:
	if (ans != '0/1'):
		ans = '-' + ans
		
print ans