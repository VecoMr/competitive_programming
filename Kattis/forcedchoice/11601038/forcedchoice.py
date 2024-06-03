n, p, s = map(int,input().split())
for _ in range(s):
    l = list(map(int,input().split()))[1:]
    print(("REMOVE","KEEP")[p in l])