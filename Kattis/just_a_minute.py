n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
r = sum(i for i, j in l)/n
r = sum(j for i, j in l)/(r*60)/n
if r == 1:
    print("measurement error")
else:
    print(r)