n = int(input())
for _ in range(n):
    i = int(input())
    l = sorted(map(int, input().split()))
    r = 0
    while l:
        l.pop(0)
        r += l.pop(0)
        l.pop(-1)
    print(r)