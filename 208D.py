n = int(raw_input())
p = raw_input()
p = p.split()

for i in range(0, len(p)):
	p[i] = int(p[i])

n = len(p)

price = raw_input()
price = price.split()

for i in range(0, 5):
	price[i] = int(price[i])
	
money = 0
items = [0, 0, 0, 0, 0]

def item(price, money):
	if (money < price[0]):
		return -1
	if (money > price[4]):
		return 4
	i = 0
	k = 0
	while (i < 5) and (price[i] <= money):
		k = i
		i += 1
	return k

i = 0
while (i < n):
	money += p[i]
	k = item(price, money)
	while (k != -1):
		t = money / price[k]
		items[k] += t
		money -= t * price[k]
		k = item(price, money)
	i += 1

items = map(str, items)
items = ' '.join(items)
print items
print money