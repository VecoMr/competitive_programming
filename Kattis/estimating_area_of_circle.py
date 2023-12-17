import math
r, m, c = map(float,input().split())
while r or m or c:
    print(math.pi*r**2, (c/m*4)*r**2)

    r, m, c = map(float,input().split())
