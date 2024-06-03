import math

n=int(input())
r=math.inf
for _ in range(n):
    y,a,b=map(int,input().split())
    r=min(r,y+a*b//math.gcd(a,b))
print(r)