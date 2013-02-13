from itertools import groupby

k = int(raw_input())
word = raw_input()

myList = list(word) # ['apple', 'banana', 'apple', 'strawberry', 'banana', 'lemon']
n = [(o, len(list(g))) for o, g in groupby(sorted(myList))]

def isvalid(n, k):
	for i in n:
		if (i[1] % k != 0):
			return False
	return True

if (isvalid(n, k) == True):
	a = ''
	ans = ''
	for i in n:
		times = i[1]/k
		for j in range(0, times):
			a = a + i[0]
	for i in range(0, k):
		ans = ans + a
else:
	ans = '-1'

print ans