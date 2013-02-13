from itertools import groupby
t = int(raw_input())

cust = []
for i in range(0, t):
	k = map(int, raw_input().split())
	cust.append(k)

freqs = [(k, len(list(g))) for k, g in groupby(sorted(cust))]

ans = 0
for e in freqs:
	if ans < e[1]:
		ans = e[1]

print ans