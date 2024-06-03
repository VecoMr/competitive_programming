n = int(input())
l = [input() for _ in range(n)]
print(*l[::2], sep="\n")