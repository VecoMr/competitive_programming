#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

int main(void)
{
    int k = 0;
    int n = 0;
    int r = 0;

    std::cin >> k;
    std::cin >> n;
    std::vector<int> tailles(n);
    std::vector<int> tailles_tri(n);
    std::map<int, std::map<int, int>> indexs{};

    std::for_each(tailles.begin(), tailles.end(), [](int &value) { std::cin >> value; });
    std::partial_sort_copy(tailles.begin(), tailles.end(), tailles_tri.begin(), tailles_tri.end());

    for (int i = 0; i < n; i++) {
        if (!indexs.count(tailles[i]))
            indexs[tailles[i]] = {};
        if (!indexs[tailles[i]].count(i % k)) {
            indexs[tailles[i]][i % k] = 1;
            r++;
        } else {
            r += indexs[tailles[i]][i % k] == 0;
            indexs[tailles[i]][i % k]++;
            r -= indexs[tailles[i]][i % k] == 0;
        }

        if (!indexs.count(tailles_tri[i]))
            indexs[tailles_tri[i]] = {};
        if (!indexs[tailles_tri[i]].count(i % k)) {
            indexs[tailles_tri[i]][i % k] = -1;
            r++;
        } else {
            r += indexs[tailles_tri[i]][i % k] == 0;
            indexs[tailles_tri[i]][i % k]--;
            r -= indexs[tailles_tri[i]][i % k] == 0;
        }
    }

    if (r)
        std::cout << "NON" << std::endl;
    else
        std::cout << "OUI" << std::endl;
    return 0;
}
