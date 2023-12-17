import math

l = [i for i in open(0)]
while l:
    n, b, h, w = map(int, l.pop(0).split())
    min_budget = math.inf
    for _ in range(h):
        price = int(l.pop(0))
        possibility = list(map(int, l.pop(0).split()))
        if price < min_budget and sum(1 for i in possibility if i >= n):
            min_budget = price
    if min_budget*n <= b:
        print(min_budget*n)
    else:
        print("stay home")