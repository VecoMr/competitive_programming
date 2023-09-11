import heapq
import math
import functools

n, s, t = map(int,input().split())

edges = [[] for _ in range(n)]

for i in range(n):
    l  = list(map(int,input().split()))
    for j in range(n):
        if i != j:
            edges[i].append((l[j],j))

heap = []
heapq.heappush(heap, (0, s))


@functools.lru_cache
def solve():
    dist = [math.inf] * n
    dist[s] = 0
    while heap:
        di, no = heapq.heappop(heap)
        for w, nd in edges[no]:
            if dist[nd] > dist[no] + w:
                dist[nd] = dist[no] + w
                heapq.heappush(heap, (dist[nd], nd))
    return dist[t]

print(solve())