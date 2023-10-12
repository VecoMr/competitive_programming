n,t = map(int,input().split())
l = sorted([int(input()) for _ in range(n)], reverse=True)
r ="YES"
for i in range(n):
    if l[i] <= t*(n-i-1):
        r = "NO"
        break
print(r)