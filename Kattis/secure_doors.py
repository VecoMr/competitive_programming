n = int(input())
l = [input().split() for _ in range(n)]
d = []
for i in l:
    m, n = i
    if m == "entry":
        if n in d:
            print(n,"entered", "(ANOMALY)")
        else:
            d.append(n)
            print(n,"entered")
    else:
        if not n in d:
            print(n,"exited", "(ANOMALY)")
        else:
            d.remove(n)
            print(n,"exited")
