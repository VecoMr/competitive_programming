n,a,b=map(int,input().split())
for _ in range(n):
    t = int(input())
    if t <= (a**2+b**2)**0.5:
        print("DA")
    else:
        print("NE")