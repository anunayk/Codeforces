def findmax(arr, n):
	ans = 0
	for i in range(0, n):
		k = max_element(arr)
		ans += arr[k]
		arr[k] -= 1
		if (arr[k] == 0):
			arr.pop(k)
	return ans

def findmin(arr, n):
	ans = 0
	for j in range(0, n):
		m = arr[0]
		k = 0
		for i in range(0, len(arr)):
			if (arr[i] < m):
				m = arr[i]
				k = i
		ans += arr[k]
		arr[k] -= 1
		if (arr[k] == 0):
			arr.pop(k)
	return ans

def max_element(a):
	m = a[0]
	k = 0
	for i in range(0, len(a)):
		if (a[i] > m):
			m = a[i]
			k = i
	return k

def min_element(a):
	m = a[0]
	k = 0
	for i in range(0, len(a)):
		if (a[i] < m):
			m = a[i]
			k = i
	return k
	
k = raw_input()
k = k.split()

n = int(k[0])
m = int(k[1])

seats = raw_input()
seats = seats.split()

i = 0
while (i < len(seats)):
	seats[i] = int(seats[i])
	i += 1

seats1 = []
for e in seats:
	seats1.append(e)
ans1 = findmax(seats, n)
ans2 = findmin(seats1, n)

print ans1, ans2

