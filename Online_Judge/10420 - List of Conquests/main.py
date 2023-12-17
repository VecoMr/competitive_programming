n = int(input())
l = [input().split()[0] for _ in range(n)]
print(*sorted([" ".join([i, str(l.count(i))]) for i in set(l)]), sep="\n")