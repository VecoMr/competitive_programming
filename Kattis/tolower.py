p, t = map(int, input().split())

r = 0
for _ in range(p):
    l = [input() for _ in range(t)]
    if sum(1 for i in l if (i[0].lower()+i[1:]).islower()) == t:
        r += 1
print(r)