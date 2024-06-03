#include <iostream>
#include <vector>
#include <algorithm>

bool is_in(std::vector<int> l, int start, int end, int n)
{
    if ((end-start)/2 == 0 && n != l[start] && n != l[end])
        return false;
    int mid = start + ((end-start)/2);
    if (l[mid] == n || l[start] == n || l[end] == n)
        return true;
    if (l[mid] > n)
        return is_in(l, start, mid, n);
    return is_in(l, mid, end, n);
}

int main(void)
{
    int n = 0, m = 0;
    std::cin >> n >> m;
    while (n || m) {
        std::vector<int> first(n);
        for (int i = 0; i < n; i++)
            std::cin >> first[i];
        std::vector<int> second(n);
        for (int i = 0; i < n; i++)
            std::cin >> second[i];
        std::vector<int> res;
        std::back_insert_iterator<std::vector<int> > it(res);
        std::set_intersection(first.begin(), first.end(), second.begin(), second.end(), it);
        std::cout << res.size() << std::endl;
        std::cin >> n >> m;
    }
}