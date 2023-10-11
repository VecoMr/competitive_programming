n = int(input())
for _ in range(n):
    i = input()
    if "simon says " in i:
        print(i[len("simon says "):])
    else:
        print()