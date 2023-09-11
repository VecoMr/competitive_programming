n = int(input())
l = []
for _ in range(n):
    a,b = input().split()
    if a.isdigit():
        l.append((int(a)/2, b))
    else:
        l.append((int(b), a))
print(*[j for i,j in sorted(l)],sep="\n")