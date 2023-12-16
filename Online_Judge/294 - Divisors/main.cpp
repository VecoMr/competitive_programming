#include <iostream>

int main(void)
{
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int x, y;
        int m = 0, o = 0;
        std::cin >> x >> y;
        for (int j = x, res = 0; j <= y; j++) {
            res = 0;
            for (int u = 1; u*u <= j; u++) {
                if (j % u == 0) {
                    res ++;
                    if (u * u < j) res ++;
                }
            }
            if (res > m) {
                m = res;
                o = j;
            }
        }
        std::cout << "Between " << x << " and " << y << ", " << o << " has a maximum of " << m << " divisors." << std::endl;
    }
}