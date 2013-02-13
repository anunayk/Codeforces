string = raw_input()
string = string.split('WUB')

ans = ''

for e in string:
	if (e != ''):
		ans = ans + ' ' + e

print ans[1:]