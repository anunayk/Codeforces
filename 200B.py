n = int(raw_input())
p = raw_input()
p = p.split()

ans = 0
for i in range(0, n):
	ans = ans + int(p[i])/100.0

ans = 100 * ans / n
print ans