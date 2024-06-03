n = int(input())
l = list(map(int, input().split()))
d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
r = 0
for i in d:
    j= d[i]
    r += j//(i+1)*(i+1)
    if j%(i+1):
        r+=i+1
print(r)
