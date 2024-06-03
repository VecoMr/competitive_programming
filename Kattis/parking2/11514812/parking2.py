n = int(input())
for _ in range(n):
    input()
    l = list(map(int,input().split()))
    print((max(l)-min(l))*2)