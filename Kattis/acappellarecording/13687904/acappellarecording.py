n, m = map(int, input().split())
l = sorted(int(input()) for _ in range(n))
a = l[0]
r = 1

for i in l[1:]:
    if i - a > m:
        a = i
        r += 1
print(r)