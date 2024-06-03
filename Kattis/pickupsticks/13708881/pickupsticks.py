from collections import deque

n, m = map(int,input().split())
dp = [1] * (n + 1)
tToB = {}
bToT = {}
for i in range(m):
    a,b = map(int, input().split())
    dp[b] = 0
    tToB.setdefault(a, [])
    bToT.setdefault(b, [])
    tToB[a].append(b)
    bToT[b].append(a)

q = deque(i for i in range(1, n+1) if dp[i])
r = []

while q:
    i = q.popleft()  # Use popleft() instead of pop(0)
    r.append(i)
    if i in tToB:
        for j in tToB[i]:
            bToT[j].remove(i)
            if not bToT[j]:
                q.append(j)

if len(r) == n:
    print(*r,sep="\n")
else:
    print("IMPOSSIBLE")