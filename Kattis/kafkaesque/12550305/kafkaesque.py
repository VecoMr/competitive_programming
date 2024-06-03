n = int(input())
tmp = 0
r = 1
for _ in range(n):
    i = int(input())
    if i < tmp: r += 1
    tmp = i

print(r)