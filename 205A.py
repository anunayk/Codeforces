n = int(raw_input())
k = raw_input()
k = k.split()

i = 0
while (i < n):
	k[i] = int(k[i])
	i += 1

mini = k[0]
ans = 1
arr = []
arr.append(ans)

i = 1
while (i < n):
	if (mini > k[i]):
		arr = []
		mini = k[i]
		ans = i+1
		arr.append(ans)
	elif (mini == k[i]):
		arr.append(i+1)
	i += 1

if (len(arr) > 1):
	print 'Still Rozdil'
else:
	print ans