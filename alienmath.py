n = int(input())
l = input().split()
l = sorted([(len(l[i]), l[i], i) for i in range(n)], reverse=True)
d = {l[i][1]:str(l[i][2]) for i in range(n)}
s = input()
t = ""
a = ""
for i in s:
    t += i
    if t in d:
        a += d[t]
        t = ""
if not a:
    print(0)
else:
    print(int(a,n))