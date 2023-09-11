n = int(input())
a,b = 1,0
for _ in range(n):
    a,b = b,b+a
print(a,b)