n = int(input())
for _ in range(n):
    l = list(map(int, [i if i != "" else "0" for i in input().split(",")]))[::-1]
    su = "+".join(f'{j}*60**{i}' for i, j in enumerate(l))
    print(eval(su))