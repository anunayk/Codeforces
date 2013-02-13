def get_palindromes(str):
	length = len(str) + 1
	found = []
	for i in xrange(0, length):
		for j in xrange(i+3, length):
			mid = i + ((j - i) / 2)
			if str[i:mid] == str[mid+1:j][::-1]:
				found.append(str[i:j])
	return found

k = raw_input()

a = get_palindromes(k)
a.sort()

print a

print a[len(a)-1]
