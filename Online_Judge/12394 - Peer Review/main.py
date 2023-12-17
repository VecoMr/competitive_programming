import math

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    d = []
    for i in range(m):
        name, *l = input().split()
        d.append([name, [int(j) for j in l]])
    dp = [0]*m
    r = 0
    for a in range(m):
        i, j = d[a]
        tmp = []
        for b in j:
            if d[b-1][0] == i or b in tmp:
                dp[b-1] = -math.inf
            else:
                dp[b-1] += 1
            tmp.append(b)
    r += sum(1 for i in dp if i != n)
    # print(dp)
    if r == 0:
        print("NO PROBLEMS FOUND")
    else:
        if r > 1:
            print(f"{r} PROBLEMS FOUND")
        else:
            print(f"1 PROBLEM FOUND")
            