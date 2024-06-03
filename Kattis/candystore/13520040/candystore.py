n,m=map(int,input().split())

d = {}
for _ in range(n):
    a, b = input().split()
    if a[0]+b[0] in d:
        d[a[0]+b[0]] = "ambiguous"
    else:
        d[a[0]+b[0]] = f'{a} {b}'
for _ in range(m):
    i = input()
    if i in d:
        print(d[i])
    else:
        print("nobody")
