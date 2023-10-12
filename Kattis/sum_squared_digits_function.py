t = int(input())
for _ in range(t):
    k, b, n = map(int, input().split())

    ssd = 0
    while n:
        digit = n % b
        ssd += digit * digit
        n //= b

    print(k, ssd)
