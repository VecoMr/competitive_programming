import math

n=int(input())
r=math.inf
for _ in range(n):
    y,a,b=map(int,input().split())
    lcm=a*b//math.gcd(a,b)
    next_year=y+lcm
    r=min(r,next_year)
print(r)