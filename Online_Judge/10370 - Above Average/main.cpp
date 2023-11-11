#include <iostream>
#include <vector>
#include <iomanip>

int main(void)
{
    int n = 0;
    int tmp;

    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int m = 0;
        std::vector<int> v;
        std::cin >> m;
        double average = 0;
        for (int j = 0; j < m; j++) {
            std::cin >> tmp;
            average += tmp;
            v.push_back(tmp);
        }
        average = average / (float) m;
        int res = 0;
        for (int j = 0; j < m; j++) {
            if (v[j] > average)
                res++;
        }
        std::cout << std::setprecision(3) << std::fixed << ((float) res / (float) m) * 100 << "%" << std::endl;
    }
}