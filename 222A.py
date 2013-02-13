r = raw_input('')
r = r.split()

n = int(r[0])
k = int(r[1])

arr = raw_input('')
arr = arr.split()

arr = map(int, arr)

if (issame(arr) == True):
	print 0
	
if ((k == 1) and (issame(arr) == False)):
	print -1

def issame(arr):
	k = arr[0]
	for i in range(0, len(arr)):
		if (arr[i] != k):
			return False
	return True

i = 0
while (issame(arr) == False) and (i < n):
	l = arr[k-1]
	arr.append(l)
	arr.pop(0)
	i += 1

if (i >= n):
	print -1
else:
	print i