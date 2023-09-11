import math
n = int(input())
def y(v, t, alpha):
    return v*t*math.sin(alpha)-(1/2)*9.81*t**2

for _ in range(n):
    v, alpha, x, h1, h2 = map(float, input().split())
    alpha = math.radians(alpha)
    t = x/(v*math.cos(alpha))
    a = y(v, t, alpha)
    # print(a, h1, h2)
    if h1+1 <= a <= h2-1:
        print("Safe")
    else:
        print("Not Safe")