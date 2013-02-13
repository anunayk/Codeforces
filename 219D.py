from itertools import groupby

n = int(raw_input())
arr = []

for i in range(0, n-1):
	k = raw_input()
	k = k.split()
	arr.append(int(k[0]))

myList = list(arr) # ['apple', 'banana', 'apple', 'strawberry', 'banana', 'lemon']
freq = [(o, len(list(g))) for o, g in groupby(sorted(myList))]

ans = (freq[len(freq)-1])[1]

s = ''
for i in range(0, len(freq)):
	if ((freq[len(freq)-1])[1] == ans):
		s = s + ' ' + str((freq[i])[0])

print n-1-ans
print s[1:]