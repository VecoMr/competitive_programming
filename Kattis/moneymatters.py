n, m = map(int,input().split())
l = [int(input()) for _ in range(n)]
a = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y = map(int,input().split())
    a[x][y] = True
    a[y][x] = True
print(*a, sep="\n")