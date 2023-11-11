n = int(input())
d = {}

t = "NONE"
for _ in range(n):
    i = input()
    d.setdefault(i, 0)
    d[i] += 1
    if d[i] > n//2:
        t = i
        break
print(t)