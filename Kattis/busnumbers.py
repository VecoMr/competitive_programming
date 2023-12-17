n = int(input())
l = sorted(map(int,input().split()))
t = None
for i in l:
    if t == None:
        t = i
        print(i, end="")
    