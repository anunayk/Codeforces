k = raw_input()
k = k.split()

n = int(k[0])
marks = int(k[1])

arr = []

for i in range(0, n):
	if (marks >= 2):
		arr.append(2)
		marks -= 2
	elif (marks == 0):
		arr.append(marks)

for i in range(0, n):
	if (marks > 0):
		arr[i] += 1
		marks -= 1

ans = 0
for i in range(0, n):
	if arr[i] <= 2:
		ans += 1

print ans