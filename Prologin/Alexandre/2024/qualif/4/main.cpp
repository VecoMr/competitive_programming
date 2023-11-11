#include <iostream>
#include <algorithm>
#include <vector>
#include <limits.h>

int main(void)
{
    int n, k, r, tmp, m;
    std::vector <int> v;
    std::cin >> n;
    std::cin >> r;
    std::cin >> k;
    for (int i = 0; i < n; i++) {
        std::cin >> tmp;
        v.push_back(tmp);
    }
    if (k >= n)
        m = *std::max_element(v.begin(), v.end());

    int j = 0;

    for (int i = 0; i < r; i++) {
        j = i%n;
        if (k < n) {
            m = INT_MIN;
            for (int l = 0; l < k; l++) {
                if (v[(j+l)%n] > m)
                    m = v[(j+l)%n];
            }
        }
        v[j] = m;
    }
    for (int i = 0; i < n; i++) {
        if (i != 0)
            std::cout << " ";
        std::cout << v[i];
    }
    std::cout << std::endl;
}