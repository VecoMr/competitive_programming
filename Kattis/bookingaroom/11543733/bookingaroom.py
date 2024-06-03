t,n = map(int,input().split())
l = [int(input()) for _ in range(n)]
if n == t:
    print("too late")
else:
    for i in range(1,t+1):
        if not i in l:
            print(i)
            break