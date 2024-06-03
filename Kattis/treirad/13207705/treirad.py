n = int(input())
a,b,c=1,2,3
res = 0
while a * b * c < n:
    res += 1
    a += 1
    b += 1
    c += 1
print(res)