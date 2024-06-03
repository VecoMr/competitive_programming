a,b = map(int, input().split())
l = [input() for i in range(b)]
if len(set(l)) != a:
    print("paradox avoided")
else:
    d = 0
    r = 0
    t = []
    while r != a:
        v = l.pop(0)
        if not v in t:
            t.append(v)
            r += 1
        d += 1
    print(d)