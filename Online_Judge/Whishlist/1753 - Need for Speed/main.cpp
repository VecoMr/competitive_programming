#include <iostream>
#include <vector>

int main(void)
{
    float n, m;

    while (std::cin >> n >> m) {
        float total_distance = 0;
        for (int i = 0; i < n; i++) {
            int d, s;
            std::cin >> d >> s;
            total_distance += d;
            m -= (float)d/(float)s;
            std::cout << d << "  " << s << " " << m << std::endl;
        }
        std::cout << total_distance/m << std::endl;

    }
}