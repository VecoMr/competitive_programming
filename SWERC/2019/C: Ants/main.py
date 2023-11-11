n = int(input())
d = [True] * (n+1)

for _ in range(n):
    i = int(input())
    if not (i < 0 or i >= n or not d[i]):
        d[i] = False

for i in range(n+1):
    if d[i]:
        print(i)
        break