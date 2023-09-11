n,p,s=map(int,input().split())
for _ in range(s): print(("REMOVE","KEEP")[p in list(map(int,input().split()))[1:]])