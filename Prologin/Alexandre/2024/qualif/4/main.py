import math

n = int(input())
r = int(input())
k = int(input())
l = list(map(int, input().split()))

m = -math.inf

if k >=n:
    m = max(l)

for i in range(r):
    i = i%n
    if k < n:
        m = -math.inf
        for j in range(k):
            if l[(i+j)%n] > m:
                m = l[(i+j)%n]
    l[i] = m
print(*l)