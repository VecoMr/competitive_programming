n = int(input())

def find_best(l, le, lc, ls, k, n, target):
    if k == le:
        return [n, ls]
    m = n
    for i in range(le):
        if i not in lc:
            tmp = find_best(l, le, lc+[i], ls+["-"] )
for _ in range(n):
    *l, target = map(int, input().split())
    if target in l:
        print("Target: {target}\nBest approx: {target}")
        continue
    