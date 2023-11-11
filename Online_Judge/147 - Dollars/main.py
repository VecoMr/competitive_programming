n = float(input().strip())

l = [0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100]

while n:
    dp = [0] * int(n/0.05)
    print()
    n = float(input().strip())
