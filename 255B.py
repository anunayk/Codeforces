def find(s, sub):
	i = 0
	while (i < len(s)-1):
		if (s[i] == sub[0]) and (s[i+1] == sub[1]):
			return i
		i += 1
	return -1

def check(s):
	k = find(s, 'yx')
	l = find(s, 'xy')
	if (k >= 0):
		return 1
	elif (l >= 0):
		return 2
	return 0


def one(s):
	k = s.index('yx')
	s = list(s)
	s[k] = 'x'
	s[k+1] = 'y'
	s = ''.join(s)
	return s

def two(s):
	k = s.index('xy')
	s = list(s)
	s.pop(k)
	s.pop(k)
	s = ''.join(s)
	return s

s = raw_input()

while (check(s)!=0):
	k = check(s)
	if (k == 1):
		s = one(s)
	elif (k == 2):
		s = two(s)

print s