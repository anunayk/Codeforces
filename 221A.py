n = int(raw_input())

ans = [n]

for i in range(1, n):
	ans.append(i)
	
ans = map(str, ans)
ans = ' '.join(ans)

print ans