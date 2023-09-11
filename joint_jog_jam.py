l, n = map(int,input().split())
r = 1
while l%n and l > n:
    print(r,l,n,l%n)
    r += 1
    n = l%n
print(r)