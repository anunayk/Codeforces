d = raw_input('')
d = d.split()
n = int(d[0])
k = int(d[1])

a = raw_input('')
a = a.split()
a = map(int, a)

i = 0
found = False
while (i < n):
	if (len(set(a[0:i])) == k):
		found = True
		break
	i += 1

if found == False:
	print -1, -1
else:
	ans1 = 1
	ans2 = i
	i = 0
	j = ans2-1
	c = 0
	while ((i < ans2) and (j >= 0)):
		if (len(set(a[i:j+1])) != k):
			break
		ans1 = i+1
		ans2 = j+1
		if (c % 2 == 0):
			i += 1
		else:
			j -= 1
		c += 1
	print ans1, ans2