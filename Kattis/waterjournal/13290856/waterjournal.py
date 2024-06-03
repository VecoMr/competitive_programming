n,a,b=map(int,input().split())
mi = False
ma = False
t = True

for _ in range(n-1):
    i = int(input())
    if i == a:
        mi = True
    if i == b:
        ma = True
    if i > b or i < a:
        t = False

t = mi or ma

if t:
    if mi and ma:
        print(*list(map(str,range(a,b+1))),sep="\n")
    if not mi:
        print(a)
    if not ma:
        print(b)
else:
    print(-1)