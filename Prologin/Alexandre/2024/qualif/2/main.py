k = int(input())
n = int(input())
l = list(map(int, input().split()))
s = sorted(l)

d = {}

for i in range(n):
    if not l[i] in d:
        d[l[i]] = {}
    if not i%k in d[l[i]]:
        d[l[i]][i%k] = 1
    else:
        d[l[i]][i%k] += 1
    if not s[i] in d:
        d[s[i]] = {}
    if not i%k in d[s[i]]:
        d[s[i]][i%k] = -1
    else:
        d[s[i]][i%k] -= 1

t = True

for i in d:
    for j in d[i]:
        if d[i][j] != 0:
            t = False
            break
    if not t:
        break

if t:
    print("OUI")
else:
    print("NON")