#include <vector>
#include <iostream>
#include <limits>

int main(void)
{
    long n = 0;

    std::cin >> n;

    std::vector<long> v(n);

    std::vector<long> dpl(n, 0);

    std::vector<long> dpr(n, 0);

    long min = 0;
    long res = std::numeric_limits<long>::min();

    for (int i = 0; i < n; i++)
    {
        std::cin >> v[i];
        if (i == 0)
        {
            min = v[i];
            continue;
        }
        dpl[i] = v[i] - min;
        if (v[i] < min || v[i - 1] > v[i])
            min = v[i];
    }
    min = v[n - 1];
    for (int i = n - 2; i >= 0; i--)
    {
        dpr[i] = v[i] - min;
        if (v[i] < min || v[i - 1] < v[i])
            min = v[i];
    }
    for (int i = 0; i < n - 1; i++)
    {
        res = std::max(res, std::min(dpl[i], dpr[i]));
    }
    std::cout << res << std::endl;
}