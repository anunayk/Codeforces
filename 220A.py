n = int(raw_input())
k = raw_input()

k = k.split()
for i in range(0, n):
	k[i] = int(k[i])

def issorted(a):
	for i in range(0, len(a)-1):
		if (a[i] > a[i+1]):
			return False
	return True

done = False
if (issorted(k) == True):
	print 'YES'
	done = True

if (done == False):
	i = 0
	while (done == False) and (i < n):
		j = i+1
		while (done == False) and (j < n):
			t = k[i]
			k[i] = k[j]
			k[j] = t
			if (issorted(k) == True):
				print 'YES'
				done = True
				break
			else:
				t = k[i]
				k[i] = k[j]
				k[j] = t
			j += 1
		if (done == True):
			break
		i += 1

if (done == False):
	print 'NO'