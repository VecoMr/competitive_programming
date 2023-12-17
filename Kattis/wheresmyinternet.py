n, m = map(int, input().split())

l = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    l[a-1].append(b-1)
    l[b-1].append(a-1)

visited = [False]*n
queue = [i for i in l[0]]
visited[0] = True

# print(queue, visited)

while queue:
    # print(visited, queue)
    i = queue.pop(0)
    if visited[i]:
        continue
    visited[i] = True
    for j in l[i]:
        if not visited[j]:
            queue.append(j)

r = [i+1 for i in range(n) if not visited[i]]

if r:
    print(*r,sep="\n")
else:
    print("Connected")
