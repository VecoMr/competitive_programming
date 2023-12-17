#include <iostream>
#include <iomanip>

int main(void)
{
    int n = 0;
    double res = 0.0000;
    std::cin >> n;
    for (int i = 0; i < n; i++)
    {
        int m = 0;
        double a[2] = {0};
        double b[2] = {0};
        double c[2] = {0};
        std::cin >> m;

        std::cin >> a[0] >> a[1];
        for (int j = 0; j < m-2; j++)
        {
            std::cin >> b[0] >> b[1];
            res += (a[0] - b[0]) * (b[1] + a[1])/2;
        }
    }
    std::cout << std::fixed << std::setprecision(1) << res << std::endl;
    return 0;
}