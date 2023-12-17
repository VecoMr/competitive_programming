import random

n = 1000
m = 600

l = []
for i in range(n):
    l.append(i)

s = "ARCM"
r = ""
for _ in range(m):

    t = s[random.randint(0,3)]
    while (t == "M" and n == 0) or (t == "C" and n == 1000):
        t = s[random.randint(0,3)]
    r += t

print(n)
print(m)
print(*l, sep="\n")
print(r)