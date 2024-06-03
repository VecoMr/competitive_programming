n,d=map(int,input().split())
l=list(map(int,input().split()))
s = [1]*n
i = 0
r = 0
while s[i]:
    r += l[i]
    s[i] = 0
    i = (i+d)%n
print(r)