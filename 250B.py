def expand(k):
    k = str(k)
    if k == "":
        return "0000"
    if (len(k) == 1):
        k = "000" + k
    elif (len(k) == 2):
        k = "00" + k
    elif (len(k) == 3):
        k = "0" + k
    else:
        k = k
    return k

n = int(raw_input())

ans = []
for i in range(0, n):
    r = raw_input()
    r = r.split(':');
    found = False
    if ("" in r):
        ind = r.index("")
        r.pop(ind)
        k = 8-len(r)
        for j in range(0, k):
            r.insert(ind, "0")
    p = ""
    for e in r:
       p = p + expand(e) +":"
    p = p[:len(p)-1]
    ans.append(p)

for e in ans:
    print e