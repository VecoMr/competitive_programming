w=int(input())
n=int(input())
for _ in range(n):
    a,b=input().split()
    if int(b) >= w:
        print(a, "opin")
    else:
        print(a, "lokud")