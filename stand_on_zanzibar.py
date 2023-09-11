n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    l.pop()
    t = l.pop(0)
    imp = 0
    while l:
        a = l.pop(0)
        if a > t*2:
            imp += a - t*2
        t = a
    print(imp)