a,b = map(int, input().split())
ind = 1
while a or b:
    dp = [0]*(a+1)
    for i in range(2, a+1):
        dp[i] = (dp[i-1]+dp[i-2]+2) % b
    print(f"Case {ind}: {a} {b} {dp[-1]+1}")
    a, b = map(int, input().split())
    ind += 1