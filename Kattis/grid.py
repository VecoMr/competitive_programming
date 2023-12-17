import math

al = [i.strip() for i in open(0)]

def bfs(grid, i, j, n, m, t, dp):
    if i == n-1 and j == m-1:
        return (True, t)
    if i < 0 or j < 0 or i >= n or j >= m or dp[i][j] == 1:
        return (False, -1)
    ma = math.inf
    dp[i][j] = 1
    # print(i,j,n,m)
    v = grid[i][j]
    dp = [a[:] for a in dp[:]]
    tmp = [bfs(grid, i+v, j, n, m, t+1, dp), bfs(grid, i, j+v, n, m, t+1, dp), bfs(grid, i-v, j, n, m, t+1, dp), bfs(grid, i, j-v, n, m, t+1, dp)]
    for x,y in tmp:
        if x:
            ma = min(ma, y)
    return (ma!=math.inf, ma)

while al:
    n, m = map(int, al.pop(0).split())
    grid = [list(map(int,al.pop(0))) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    b, t = bfs(grid, 0, 0, n, m, 0, visited)
    if b:
        print(t)
    else:
        print(-1)
    
    