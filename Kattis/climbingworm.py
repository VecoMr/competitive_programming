a,b,h=map(int,input().split())
r = 0
t = 0
while r < h:
    r += a
    t+= 1
    if r >= h:
        break
    r -= b
print(t)