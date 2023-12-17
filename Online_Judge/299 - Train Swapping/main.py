n = int(input())
def issorted(l):
    tmp = -10
    for i in l:
        if i < tmp:
            return False
        tmp = i
    return True

for _ in range(n):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    while not issorted(a):
        for i in range(1, n):
            if a[i-1] > a[i]:
                a[i], a[i-1] = a[i-1], a[i]
                res += 1
    print(f"Optimal train swapping takes {res} swaps.")
