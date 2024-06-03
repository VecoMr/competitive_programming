n = int(input())
l = [[int(i) for i in input().split()] for _ in range(n)]
t = True
a = 0
for i,j in l:
    a += i
    if a < j:
        t = False
        break
print(("impossible", "possible")[t])
