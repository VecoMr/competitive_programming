s, n = map(int, input().split())
r = 0
t = 1
while n:
    if 2**t <= n:
        t += 1
    else:
        n -= 2**(t-1)
        t = 1
        r += 1
print(r)
