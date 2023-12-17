#include <iostream>
#include <vector>

int main(void)
{
    int n = 0;
    int nb = 0;
    std::cin >> n;
    while (n) {
        nb += 1;
        int tmp = 0;
        int sum = 0;
        int res = 0;
        std::vector<int> v;
        for (int i = 0; i < n; i++) {
            std::cin >> tmp;
            sum += tmp;
            v.push_back(tmp);
        }
        sum = sum / n;
        for (int i = 0; i < n; i++) {
            if (v[i] > sum) {
                res += v[i] - sum;
            }
        }
        std::cout << "Set #" << nb << std::endl;
        std::cout << "The minimum number of moves is " << res << ".\n" << std::endl;
        std::cin >> n;
    }
}