w = int(input())
n = int(input())
l = 0
for _ in range(n):
    a,b = map(int,input().split())
    l += a*b
print(l//w)
