import math
n = int(input())
for _ in range(n):
    m = int(input())
    l = [tuple(map(int, input().split())) for _ in range(m)]
    print(sum([max(0,min(10, 11-math.ceil((i*i+j*j)**0.5/20))) for i,j in l]))