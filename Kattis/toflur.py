n = int(input())
l = sorted(map(int,input().split()))
r = 0
for i in range(1, n):
    r += (l[i]-l[i-1])**2
print(r)