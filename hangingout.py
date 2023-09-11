n, m = map(int, input().split())
r = 0
c = 0
for _ in range(m):
    a, b = input().split()
    b = int(b)
    if a == "enter":
        if c + b > n:
            r += 1
        else:
            c += b
    if a == "leave":
        c -= b
print(r)