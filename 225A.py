n = int(raw_input())

top = int(raw_input())
bottom = 7 - top

arr = []
for i in range(0, n):
	r = raw_input()
	r = r.split()
	r = map(int, r)
	arr.append(r)

for i in range(0, n):
	(arr[i]).append(7-(arr[i])[0])
	(arr[i]).append(7-(arr[i])[1])

ans = ''
i = 1
while (i < n):
	if bottom in arr[i]:
		ans = 'NO'
		break
	else:
		bottom = 7 - bottom
	i += 1

if ans != 'NO':
	ans = 'YES'

print ans