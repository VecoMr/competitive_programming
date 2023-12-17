#include <vector>
#include <iostream>

int dijkstra(int start, int target, std::vector<std::vector<int> > graph, int n)
{
    std::vector<int> visited(n, 0);
    
}

int main(void)
{
    int n, m, q, s = 0;
    int u, v, w = 0;
    int query = 0;
    std::cin >> n >> m >> q >> s;

    while (n || m || q || s) {
        std::vector<std::vector<int> > graph(n, std::vector<int>(n, 0));

        for (int i = 0; i < m; i++) {
            std::cin >> u >> v >> w;
            graph[u][v] = w;
        }

        for (int i = 0; i < q; i++) {
            std::cin >> query;
            std::cout << query;
        }
        std::cin >> n >> m >> q >> s;
    }
}