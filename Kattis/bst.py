n, *l = map(int, input().split())
total = 0
l = []
all_dist = [0] * (n + 2)

for i in l:
    l.append(i)
    l1 = sorted(l)
    ind = l1.index(i)
    
