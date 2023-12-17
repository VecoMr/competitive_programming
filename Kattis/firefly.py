n,h = map(int, input().split())
l = [int(input()) for _ in range(n)]

def calcul(nb, m):
    r = 0
    for i in range(n):
        if m != None and r > m:
            return m +1
        if (i%2 and l[i] >= nb) or (i%2 == 0 and h-l[i] < nb):
            r += 1
    return r

m = [None, 0]
for i in range(h):
    t = calcul(i+1, m[0])
    if m[0] == None or m[0] > t:
        m[0] = t
        m[1] = 1
    elif m[0] == t:
        m[1] += 1

print(*m)

