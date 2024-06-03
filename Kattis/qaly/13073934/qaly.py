n = int(input())
r = 0
for _ in range(n):
    a,b=map(float,input().split())
    r += a*b
print(r)