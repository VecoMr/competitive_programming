n = int(input())
for _ in range(n):
    n, p = input().split()
    p = int(p)
    print(n, p*(p+1)//2, p**2, p*(p+1))