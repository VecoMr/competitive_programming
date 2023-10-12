n = int(input())
l = [(0, 1)]
for i,j in zip(range(2, 1+n), map(int,input().split())):
    l.append((j,i))
print(*[i[1] for i in sorted(l)])