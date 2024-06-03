n, m = map(int, input().split())

grid = [input() for _ in range(n)]
dp = [[0]*m for _ in range(n)]

def e(i, j, grid, n, m, dp):
    if i < 0 or j < 0 or i >= n or j >= m:
        return
    if (grid[i][j] == "L" or grid[i][j] == "C") and dp[i][j] == 0:
        dp[i][j] = 1
        e(i-1, j, grid, n, m, dp)
        e(i, j-1, grid, n, m, dp)
        e(i+1, j, grid, n, m, dp)
        e(i, j+1, grid, n, m, dp)
res = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "L" and dp[i][j] == 0:
            res += 1
            e(i,j,grid,n,m,dp)
print(res)