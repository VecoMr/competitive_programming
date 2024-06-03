n,m=map(int,input().split())
l=list(map(int,input().split()))
r=0
for i in range(m,n+1):
    if sum((j+1)%2 for j in l[i-m:i]) >= 2:
        r+=1
print(r)