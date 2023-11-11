n = int(input())

for _ in range(n):
    m = int(input())
    dp = [0]*(m+1)
    a = 1
    b = 1
    c = 0
    # print(dp)
    for i in range(2, m+1):
        dp[i] = dp[i-1]+dp[i-2]+2
        c = b + a
        a = b
        b = c
    # print(dp)
    print(f"fib({m}) = {dp[-1]} calls = {a}")