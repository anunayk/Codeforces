k = raw_input()
k = k.split()
k = map(int, k)

a = k[0]
b = k[1]
c = k[2]

ans = a * c

if (ans % b == 0):
	ans = ans/b
	ans = ans - c
else:
	ans = ans/b + 1
	ans = ans - c

print ans