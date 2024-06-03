n = int(input())
d = {}
for _ in range(n):
    a,b = input().split()
    d.setdefault(a, 0)
    d[a] += int(b)

print(sorted(d, key=lambda x: d[x])[-1])