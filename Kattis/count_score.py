n = int(input())
l = []
for _ in range(n):
    a,b,c,d = input().split()
    l.append((int(a), f'{b} {c}', float(d)))
print(l)
print(1/5*sum((1-1/5)**i * l[i][-1] for i in range(n)))