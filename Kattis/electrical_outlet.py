n = int(input())
for i in range(n):
    a, *l = map(int,input().split())
    print(sum(l)-len(l)+1)