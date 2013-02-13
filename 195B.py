k = raw_input()
k = k.split()
k = map(int, k)

n = k[0]
m = k[1]

arr = m * [0]
ans = n * [0]

def get_basket(arr):
	m = arr[0]
	for i in range(0, len(arr)):
		if (arr[i] < m):
			m = arr[i]
	new = []
	for i in range(0, len(arr)):
		if (arr[i] == m):
			new.append(i+1)
	print new
	if (len(new) == 1):
		return new[0]
	else:
		m = (len(arr) + 1)/2 - new[0]
		new1 = []
		for i in range(0, len(new)):
			if ( m > abs((len(arr) + 1)/2 - new[i])):
				m = abs((len(arr) + 1)/2 - new[i])
		for i in range(0, len(new)):
			if ( m == abs((len(arr) + 1)/2 - new[i])):
				new1.append(new[i])
		print new1
		if (len(new1) == 1):
			return new1[0]
		else:
			if (new1[0] < new1[1]):
				return new1[0]
			else:
				return new1[1]

for i in range(0, n):
	k = get_basket(arr)
	print 'arr =', arr
	arr[k-1] += 1
	print k