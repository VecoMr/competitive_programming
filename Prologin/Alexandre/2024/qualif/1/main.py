import math

n = int(input())
l = list(map(int, input().split()))

r = 0

m = -math.inf
bigest_up = 0

curr = 0

for i in l:
    if i > bigest_up:
        bigest_up = i

    curr += i
    if curr > m:
        m = curr
        r = bigest_up

print(r)