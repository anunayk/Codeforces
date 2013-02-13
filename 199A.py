def f(n):
	if (n == 0):
		return [0]
	elif (n == 1):
		return [0, 1, 1]
	else:
		a = 0
		b = 1
		arr = [a, b]
		c = a + b
		while (c <= n):
			arr.append(c)
			a = b
			b = c
			c = a + b
		return arr	

n = int(raw_input())
k = f(n)
ans = []
done = False

i = 0
while (i < len(k)) and (done == False):
	a = n - k[i]
	if (a in k):
		j = 0
		l = f(a)
		while (j < len(l)) and (done == False):
			b = a - l[j]
			if (b in l):
				done = True
				ans.append(b)
				ans.append(k[i])
				ans.append(l[j])
			j += 1
	i += 1

if (done == True):
	ans.sort()
	ans = map(str, ans)
	ans = ' '.join(ans)
	print ans
else:
	print 'I\'m too stupid to solve this problem'
		