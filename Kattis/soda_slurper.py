e,f,c = map(int, input().split())
t = e+f
r = 0
while t >= c:
    t -= c
    r += 1
    t += 1
print(r)