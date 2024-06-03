l = sorted(list(map(int,input().split())))
d = {"A" : 0, "B":1, "C":2}
print(*[l[d[i]] for i in input()])
