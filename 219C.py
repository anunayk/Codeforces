i = raw_input()
i = i.split()

n = int(i[0])
k = int(i[1])

string = raw_input()
string = list(string)

color = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
color = color[:k]

c = 0
for i in range(1, n-1):
	if (string[i] == string[i+1]):
		c += 2

print c/2

def getcolor(c, k):
	color = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	color = color[:k]
	if (c != 'A'):
		return 'A'
	else:
		return 'B'

for i in range(1, n-1):
	if (string[i] == string[i+1]):
		string[i] = getcolor(string[i], k)

string = ''.join(string)
print string
		