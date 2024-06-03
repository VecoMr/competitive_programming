n = int(input())
l = list(map(int, input().split()))
dp = [2] * 7
for i in l:
    if dp[i]: dp[i] -= 1
for i in range(6,-1,-1):
    if dp[i] == 1:
        print(l.index(i)+1)
        exit(0)
print("none")