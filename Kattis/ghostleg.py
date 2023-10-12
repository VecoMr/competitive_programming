n, m = map(int,input().split())
pos = list(range(1, 1+n))

for _ in range(m):
    i = int(input())
    pos[i], pos[i-1] = pos[i-1], pos[i]

print(*pos, sep="\n")