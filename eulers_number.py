n = int(input())
e = 0
t = 1
for i in range(n+1):
    if i > 0:
        t *= i
        e += 1/t
    else:
        e += 1
print(e)