s=[int(i) for i in input()]
r = 0
t = 1
m = 0
for i in s:
    if i:
        if not t:
            t = 1
            r = max(r, m)
            m= 0
    else:
        t = 0
        m += 1
print(r//2+r%2)