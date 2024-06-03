n=int(input())
d={input():0 for _ in range(n)}
m=int(input())
for _ in range(m):
    k,*l=input().split()
    for i in l:
        d[i]+=1
print(*[f"{d[i]} {i}" for i in sorted(d, key=lambda x: x[1], reverse=True)],sep="\n")