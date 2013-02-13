def kgen(k, n):
	arr = [0, 1]
	i = 0
	while (arr[len(arr)-1] < n):
		if len(arr) < k:
			s = 0
			for j in range(0, len(arr)):
				s += arr[j]
			arr.append(s)
		else:
			s = 0
			j = len(arr)-1
			while (j >= len(arr)-k):
				s += arr[j]
				j -= 1
			arr.append(s)
		i += 1
	arr.remove(1)
	return arr
	
def encode(n, k):
	# Return string with Fibonacci encoding for n (n >= 1).
	result = ""
	if n >= 1:
		fibs = kgen(k, n)
		result = ""  # extra "1" at end
		for fibnum in reversed(fibs):
			if n > fibnum:
				n = n - fibnum
				result = "1" + result
			elif (n == fibnum):
				if (len(result) < 2):
					result = "0" + result
				else:
					n = n - fibnum
					result = "1" + result
			else:
				result = "0" + result
		ans = []
		result = list(result)
		for i in range(0, len(result)):
			if (result[i] == '1'):
				ans.append(fibs[i])
	return ans
 
t = raw_input()
t = t.split()
t = map(int, t)

ans = encode(t[0], t[1])
ans = map(str, ans)

print len(ans)
print ' '.join(ans)