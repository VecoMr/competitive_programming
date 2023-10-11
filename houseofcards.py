n = int(input())
a = 2*(n*(n+1)//2) + (n*(n-1)//2)
while a%4:
    n += 1
    a += n*2+n-1
print(n)