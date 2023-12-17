n = int(input())
for j in range(n):
    a, b = map(int, input().split())
    l = list(range(1, a + 1))
    i = 0
    while a > 1:
        i = (i + b - 1) % a
        del l[i]
        a -= 1
    print(f'Case {j+1}: {l[0]}')