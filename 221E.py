n = int(raw_input())
a = raw_input()
b = raw_input()

a = a.split()
b = b.split()

a1 = n * [0]
b1 = n * [0]

for i in range(0, n):
	a[i] = int(a[i])
	b[i] = int(b[i])
	a1[a[i]-1] = i+1
	b1[b[i]-1] = i+1

def cyclicshift(arr, n):
	k = arr[n:]
	k = k + arr[:i]
	return k

#def linear_search(a, key):
#	for i in range(0, len(a)):
#		if (a[i] == key):
#			return i

def indices(a, n, k):
	for i in range(0, n):
		if (a[i] > k):
			a[i] -= k
		else:
			k = k - a[i]
			a[i] = n - k
	return a
		
def distance(a1, b1, n, k):
#	print a1
#	print b1
#	print '-'
#	b1 = indices(b, n, k)
	m = abs(a1[0] - b1[0])
	for i in range(0, len(a)):
		if (abs(a1[i] - b1[i]) < m):
			m = abs(a1[i] - b1[i])
			if (m == 0):
				return m
	return m

for i in range(0, n):
	k = cyclicshift(b, i)
	for j in range(0, n):
		b1[k[j]-1] = j+1
	print distance(a1, b1, n, i)

	