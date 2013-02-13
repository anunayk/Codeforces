sqr = []
for i in range(0, 3):
	r = map(int, raw_input().split())
	sqr.append(r)
	
a = 0
b = sqr[1][0] + sqr[2][0] - sqr[0][1] - sqr[2][1]
c = sqr[1][0] + sqr[2][0] - sqr[0][2] - sqr[1][2]

a = (sqr[1][0] + sqr[2][0] - b - c)/2
b = a + b
c = a + c

sqr[0][0] = a
sqr[1][1] = b
sqr[2][2] = c

for e in sqr:
	print ' '.join(e)