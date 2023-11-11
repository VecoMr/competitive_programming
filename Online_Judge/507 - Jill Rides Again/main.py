import math

n = int(input())

for k in range(n):
    m = int(input())
    l = [int(input()) for _ in range(m-1)]
    dp = [[0 for _ in range(m-1)] for _ in range(m+1)]
    max_res = 0
    coords = (-1, -1)

    for i in range(1, m):
        for j in range(m - i):
            dp[i][j] = dp[i-1][j] + l[j+i-1]
            if dp[i][j] > max_res or (dp[i][j] == max_res and i > coords[0]):
                max_res = dp[i][j]
                coords = (i,j)
    # for i in dp:
    #     print(*i)

    # print(max_res, coords)


    if max_res != 0:
        print(f"The nicest part of route {k+1} is between stops {coords[1]+1} and {coords[1]+1+coords[0]}")
    else:
        print(f"Route {k+1} has no nice parts")


