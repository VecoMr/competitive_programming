n = int(input())
l = list(map(int,input().split()))
m = 0
i = 0
while i < n:
    t = i
    delta = 0
    while i < n:
        i += 1
        if i >= n:
            break
        if l[i] >= l[t]:
            if delta > m:
                m = delta
            break
        delta += 1
l = l[::-1]
i = 0
while i < n:
    t = i
    delta = 0
    while i < n:
        i += 1
        if i >= n:
            break
        if l[i] >= l[t]:
            if delta > m:
                m = delta
            break
        delta += 1
print(m)