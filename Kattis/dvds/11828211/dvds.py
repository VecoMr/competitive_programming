n = int(input())
for _ in range(n):
    m = int(input())
    l = list(map(int, input().split()))
    r = 0
    t = 1
    for j in l:
        if j != t:
            r += 1
        else:
            t += 1
    print(r)