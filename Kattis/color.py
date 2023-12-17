s, c, k = map(int, input().split())
l = sorted(list(map(int, input().split())))
a, b = 0, min(c-1, s-1)
r = 0
while a < s:
    if l[b] - l[a] <= k:
        r += 1
        a, b = b+1, min(b+c, s-1)
    else:
        b -= 1
print(r)
    