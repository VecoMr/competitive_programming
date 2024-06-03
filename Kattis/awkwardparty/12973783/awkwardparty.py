n = int(input())
l = list(map(int,input().split()))

p = {i:-1 for i in l}
m = [n] * n

for i, j in enumerate(l):
    if p[l[i]] == -1:
        p[l[i]] = i
    else:
        m[i] = i - p[l[i]]
        p[l[i]] = i
print(min(m))