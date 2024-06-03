n, *l = map(int,open(0))
l.sort(reverse=True)
l = sum([sum(l[i:i+2]) for i in range(0,n,3)])
print(l)