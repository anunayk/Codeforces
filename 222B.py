r = raw_input('')
r = r.split()

n = int(r[0])
m = int(r[1])
k = int(r[2])

mat = []

for i in range(0, n):
	arr = raw_input('')
	arr = arr.split()
	arr = map(int, arr)
	mat.append(arr)

ans = []
for i in range(0, k):
	k = raw_input('')
	k = k.split()
	x = int(k[1])-1
	y = int(k[2])-1
	if (k[0] == 'g'):
		ans.append((mat[x])[y])
	elif (k[0] == 'r'):
		t = mat[x]
		mat[x] = mat[y]
		mat[y] = t
	else:
		for i in range(0, n):
			t = (mat[i])[x]
			(mat[i])[x] = (mat[i])[y]
			(mat[i])[y] = t

for e in ans:
	print e
			