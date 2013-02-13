name = raw_input('')
name = list(name)
name = set(name)

if (len(name) % 2 == 1):
	print 'IGNORE HIM!'
else:
	print 'CHAT WITH HER!'