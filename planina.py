n = int(input())
c = 2
t = 4
for i in range(n):
    t = t*4-(c*2-1)*2-1
    c = c*2-1

print(t)