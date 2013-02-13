from math import *

r = raw_input('')
r = r.split()

r = map(int, r)

ans = 0
a = sqrt((r[1] * r[2]) / r[0])
b = r[1] / a
c = r[2] / a

ans = 4 * (a + b + c)
print int(ans)