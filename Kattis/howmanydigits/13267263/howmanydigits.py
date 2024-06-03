import math
import math

dp = [0] * 1_000_001
dp[0] = 1
l = 1
for i in range(1, 1_000_001):
    l += math.log10(i)
    dp[i] = int(l)

for i in map(int,open(0)):
    print(dp[i])