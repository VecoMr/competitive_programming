n = int(input())
l = [1, 1]
while l[-1] < n:
    l.append(l[-1] + l[-2])
r = []

for i in l[::-1]:
    if i <=n:
        r.append(i)
        n -= i
        if not n:
            break

print(*r[::-1])