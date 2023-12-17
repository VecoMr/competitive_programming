n = int(input())
l = []
for _ in range(n):
    i = input()
    a = len(i)
    if a != len(set(i)):
        continue
    if a < 5:
        continue
    l.append((a, i))

if l:
    m = min(l)[0]
    print(sorted(i[1] for i in l if i[0] == m)[-1])
else:
    print("neibb!")