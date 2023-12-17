from typing import List

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.is_trap = False
        self.is_key = False
        self.paths = []
        self.neighbors = []
        self.d = 0

class Graph:
    def __init__(self, n):
        self.nodes = [Node(i) for i in range(1, n + 1)]
        self.edges = {}
    
    def add_edge(self, u, v, w):
        self.edges[(u-1, v-1)] = w
        self.edges[(v-1, u-1)] = w
        self.nodes[u - 1].neighbors.append(self.nodes[v - 1])
        self.nodes[v - 1].neighbors.append(self.nodes[u - 1])

    def min_to(self, s, e, t):
        visited = [False] * len(self.nodes)
        visited[t.val - 1] = True
        queue = [(0, s)]
        res = 0
        print(self.edges)
        while queue:
            # print(queue)
            dist, node = queue.pop(0)
            if not visited[node.val - 1]:
                visited[node.val - 1] = True
                for neigh in node.neighbors:
                    # print(neigh.val, neigh.d)
                    if not visited[neigh.val - 1]:
                        queue.append((dist + self.edges[(node.val - 1, neigh.val - 1)], neigh))
                        neigh.d = dist + self.edges[(node.val - 1, neigh.val - 1)]
                        neigh.paths.append(node)
                        res += self.edges[(node.val - 1, neigh.val - 1)]
                        queue.sort(key=lambda x: x[0])
        return res


n, q = map(int,input().split())

graph = Graph(n)

for _ in range(n - 1):
    u, v, w = map(int,input().split())
    if u != v:
        graph.add_edge(u, v, w)

for _ in range(q):
    s, k, t = map(int,input().split())
    print(graph.min_to(graph.nodes[s - 1], graph.nodes[k - 1], graph.nodes[t - 1]))
    for i in graph.nodes:
        print([j.val for j in i.paths])

