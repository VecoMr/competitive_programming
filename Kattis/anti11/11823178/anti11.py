n, *l = map(int,open(0))
m = max(l)
dp = [[1,0]]*(m+1)
C = 10**9+7
for i in range(1,m+1):
    dp[i] = [sum(dp[i-1]), dp[i-1][0]]
for i in l:
    if i == 0:
        print(i)
    else:
        print(sum(dp[i])%C)