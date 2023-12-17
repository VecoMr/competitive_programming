from heapq import heappop, heapify, heappush
n, m, q, s = map(int, input().split())

def dijkstra(start, target, graph, n):
    visited = [[False, 0] for _ in range(n)]
    queu = [(0, start)]
    heapify(queu)
    # print(queu)
    res = -1
    while queu:
        dist, node = heappop(queu)
        if node == target:
            res = dist
            break
        if not (visited[node][0]):
            visited[node][0] = True
            visited[node][0] = dist
            for i in graph[node]:
                if not visited[i][0]:
                    heappush(queu, (dist + graph[node][i], i))
    return res

tmp = False

while n or m or q or s:
    graph = [{} for _ in range(n)]
    for i in range(m):
        u, v, w = map(int, input().split())
        graph[v][u] = w

    if tmp:
        print()
    else:
        tmp = not tmp

    for i in range(q):
        query = int(input())
        dij = dijkstra(query, s, graph, n)
        if dij == -1:
            print("impossible")
        else:
            print(dij)
    # print(graph)

    n, m, q, s = map(int, input().split())