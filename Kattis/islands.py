n = int(input())
for _ in range(n):
    m, *l = map(int, input().split())
    r = 0
    t = [0]
    for i in l:
        if not i in t:
            r += 1
            t.append(i)
            t = sorted(t)
        while t and t[-1] > i:
            t.pop(-1)
    print(m,r)