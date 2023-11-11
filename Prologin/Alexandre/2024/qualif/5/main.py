n = int(input())
dieux = [input().split() for _ in range(n)]
m = int(input())
links = [input().split() for _ in range(m)]

mat = [[] for _ in range(n)]

mat_poss = [[] for _ in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        if dieux[i][0] == dieux[j][0] or dieux[i][1] == dieux[j][1]:
            mat_poss[i].append(j)
            mat_poss[j].append(i)

for a, b, c, d in links:
    g = dieux.index([a, b])
    h = dieux.index([c, d])
    mat[g].append(h)
    mat[h].append(g)

print(mat_poss)
print(mat)

def is_possible(mat, poss, visited, queue):
    while queue:
        next = queue.pop(0)
        if not visited[next]:
            visited[next] = True
            queue = mat[next] + queue
    print(visited)

for i in range(n):
    visited = [False] * n
    is_possible(mat, mat_poss, visited, [i])


