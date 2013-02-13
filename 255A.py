def max(a, b, c):
	if ((a >= b) and (a >= c)):
		return 0
	elif ((b >= a) and (b >= c)):
		return 1
	else:
		return 2

n = int(raw_input())

exercise = map(int, raw_input().split())
muscles = [0, 0, 0]

i=0
while (i < n):
	muscles[i%3] += exercise[i]
	i+=1

if max(muscles[0], muscles[1], muscles[2]) == 0:
	print "chest"
elif max(muscles[0], muscles[1], muscles[2]) == 1:
	print "biceps"
else:
	print "back"

