while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    n, l = data[0], data[1:]
    dp = [[1, [l[i]]] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j] and (dp[i][0] < dp[j][0] + 1 or (dp[i][0] == dp[j][0] + 1 and dp[j][1] + [l[i]] < dp[i][1])):
                dp[i] = [dp[j][0] + 1, dp[j][1] + [l[i]]]
    m, s = max(dp, key=lambda x: (x[0], -l.index(x[1][0])))
    print(m, ' '.join(map(str, s)))