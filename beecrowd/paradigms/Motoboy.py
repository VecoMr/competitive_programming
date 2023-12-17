n = int(input())
while n:
    m = int(input())
    dp = [0] * (m+1)
    l = sorted([list(map(int, input().split()))[::-1] for _ in range(n)], reverse=True)
    for b, a in l:
        for j in range(m, 0, -1):
            if j - b == 0:
                dp[j] = max(dp[j], a)
            if j - b > 0 and dp[j - b]:
                dp[j] = max(dp[j], dp[j-b]+a)
    n = int(input())
    print(f"{max(dp)} min.")
