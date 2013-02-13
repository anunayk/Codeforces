t = int(raw_input())

count = 0
for i in range(0, t):
	k = map(int, raw_input().split())
	one = 0
	for j in k:
		if j==1:
			one+=1
	if one>=2:
		count+=1

print count