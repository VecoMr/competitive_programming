n = int(input())
l = list(map(int,input().split()))
last = [1] * l[0]
s = l[0]
r = [last[:]]
for i in range(1, n):
    t = l[i]
    if s > t:
        del last[t:]
        last[t-1] += 1
        r.append(last[:])
    else:
        last = last + [1] * (t-s)
        r.append(last[:])
    s = t
print(*["".join(map(str,i)) for i in r])