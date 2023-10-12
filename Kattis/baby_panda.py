n, m = map(int,input().split())
a = 0
while m%2 == 0:
    m //= 2
    a += 1
print(a)