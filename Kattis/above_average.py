n = int(input())
for _ in range(n):
    a, *l = map(int,input().split())
    av = sum(l) / a
    print("%.3f" % (sum(1 for i in l if i > av)/a*100)+"%")