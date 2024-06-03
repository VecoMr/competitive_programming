n, m = map(int, input().split())

for i in range(1, int(m**0.5)+1):
    if m % i == 0 and 4 + (m // i)*2 + i*2 == n:
        print(m//i+2, i+2)