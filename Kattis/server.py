n,t = map(int,input().split())
l = list(map(int,input().split()))
r = 0
while l and t-l[0] >= 0:
    r += 1
    t -= l.pop(0)
print(r)