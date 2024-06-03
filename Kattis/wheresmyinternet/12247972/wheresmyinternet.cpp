#include <iostream>
#include <queue>
#include <vector>

int main(void)
{
    int n = 0, m = 0;
    std::cin >> n >> m;
    std::vector<std::vector<int> > graph(n);
    int a = 0, b = 0;
    for (int i = 0; i < m; i++) {
        std::cin >> a >> b;
        graph[a-1].push_back(b-1);
        graph[b-1].push_back(a-1);
    }
    std::vector<bool> visited(n, false);
    visited[0] = true;
    std::queue <int> q;
    for (int i = 0; i < graph[0].size(); i++)
        q.push(graph[0][i]);
    int i = 0;
    while (q.size() > 0) {
        i = q.front();
        q.pop();
        if (visited[i])
            continue;
        visited[i] = true;
        for (int j = 0; j < graph[i].size(); j++) {
            if (!visited[graph[i][j]])
                q.push(graph[i][j]);
        }
    }
    
    bool r = true;
    for (int j = 0; j < n; j++) {
        if (!visited[j]) {
            r = false;
            break;
        }
    }
    if (!r) {
        for (int j = 0; j < n; j++) {
            if (!visited[j]) {
                std::cout << j+1 << std::endl;
            }
        }
    } else {
        std::cout << "Connected" << std::endl;
    }
}