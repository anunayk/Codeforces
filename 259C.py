def compare(bin1, bin2):
	i = 0
	while (i < len(bin1)):
		if (int(bin1[i]) > int(bin2[i])):
			return bin1
		elif (int(bin1[i]) < int(bin2[i])):
			return bin2
		i += 1
	return bin1

bin = list(raw_input())

m = bin[1:]
i = 0
while (i < len(bin)):
	k = bin[:i] + bin[i+1:]
	m = compare(m, k)
	i += 1

print ''.join(m)