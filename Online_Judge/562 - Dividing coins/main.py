n = int(input())
for _ in range(n):
    m = int(input())
    l = list(map(int, input().split()))
    su = sum(l)
    target = su//2
    dp = [False for _ in range(target+1)]
    dp[0] = True
    for i in range(m):
        for j in range(target, 0, -1):
            if j-l[i] >= 0 and dp[j-l[i]]:
                dp[j] = True
    for i in range(target, -1, -1):
        if dp[i]:
            print(su-i*2)
            break
