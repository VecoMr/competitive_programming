a,b = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(a)]
r = b
for i,j in l:
    if i<= r <= j:
        r+=1

print(r)