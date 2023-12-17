n, m = map(int, input().split())

while n or m:
    l = [int(input()) for _ in range(n)]
    r = 0
    for _ in range(m):
        i = int(input())
        for j in l:
            if i == j:
                r += 1
                break
            if j > i:
                break
    n, m = map(int, input().split())
    