n = int(input())
for _ in range(n):
    a, *l = map(int,input().split())
    s = sum(l[i]*l[i+3] - l[i+1]*l[i+2] for i in range(0,(a-1)*2, 2)) + (l[0]*l[-2] - l[1]*l[-2])
    print(s/2)