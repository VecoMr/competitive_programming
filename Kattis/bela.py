n, c = input().split()
n = int(n)
d = {"A": [11, 11], "K":[4, 4], "Q":[3, 3], "J":[20, 2], "T":[10, 10], "9":[14, 0], "8":[0, 0], "7":[0, 0]}
r = 0
for _ in range(n*4):
    a, b = list(input())
    r += d[a][c!=b]
print(r)