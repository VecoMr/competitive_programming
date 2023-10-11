import math
n = int(input())
l = list(map(int,input().split()))
dp = [True]*n
a = -math.inf
b = math.inf
for i in range(n):
    dp[i] = dp[i] and a <= l[i]
    a = max(a, l[i])
    dp[n-i-1] = dp[n-i-1] and b > l[n-i-1]
    b = min(b, l[n-i-1])
print(sum(dp))