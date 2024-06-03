n = int(input())
r = 0
while sum(i**2 for i in range(1,r*2+2,2)) <= n:r += 1
print(r)