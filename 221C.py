n = int(raw_input())
arr = raw_input()
arr = arr.split()
newarr = []

for i in range(0, n):
	arr[i] = int(arr[i])
	newarr.append(arr[i])
	
newarr.sort()

count = 0
for i in range(0, n):
	if (arr[i] != newarr[i]):
		count += 1

if (count < 3):
	print 'YES'
else:
	print 'NO'
