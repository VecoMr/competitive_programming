import math
n = int(input())
def e(n, k):
    if n <= 0:
        return [n, k]
    m = [-math.inf, math.inf]
    for i in [100, 200, 500]:
        a, b = e(n-i, k+1)
        if (a == m[0] and b < m[1]) or a > m[0]:
            m = [a, b]
    return m
print(e(n, 0)[1])