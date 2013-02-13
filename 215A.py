n1 = int(raw_input())
a = raw_input()
a = a.split()
a = map(int, a)

n2 = int(raw_input())
b = raw_input()
b = b.split()
b = map(int, b)

m = 0
count = 1

for j in a:
	for i in b:
		if (i >= j):
			if (i % j == 0):
				if (i/j > m):
					m = i/j
					count = 1
				elif (i/j == m):
					count +=1
print count