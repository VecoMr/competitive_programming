r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
res = [0] * 5

for i in range(1, r):
    for j in range(1, c):
        s = grid[i-1][j-1:j+1] + grid[i][j-1:j+1]
        if "#" in s:
            continue
        res[s.count("X")] += 1
print(*res,sep="\n")