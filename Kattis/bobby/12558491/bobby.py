from math import comb
n = int(input())
for _ in range(n):
    min_value, sides, x, y, multp = map(int, input().split())
    p = (sides - min_value + 1) / sides
    print(("no","yes")[(multp * sum(comb(y, i) * p**i * (1-p)**(y-i) for i in range(x, y+1))) > 1])