def check(s):
	k = set(s)
	if (len(s) == len(k)):
		return 1
	else:
		return 0

i = int(raw_input())

ans = i+1
while (True):
	if (check(list(str(ans))) == 1):
		print ans
		break
	ans += 1