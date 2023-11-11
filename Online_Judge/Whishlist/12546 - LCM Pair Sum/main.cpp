#include <iostream>
#include <numeric>
#include <vector>

int gcd(int a, int b)
{
    while (true) {
        if (a == 0)
            return b;
        b %= a;
        if (b == 0)
            return a;
        a %= b;
    }
}

int lcm(int a, int b) {
    int x = gcd(a,b);
    if (x)
        return abs(a*b)/x;
    return 0;
}

int main(void)
{
    int n;
    int m;
    int a, b;
    int x;
    int r;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        x = 1;
        r = 0;
        std::cin >> m;
        std::vector <int> v;
        v.push_back(1);
        for (int j = 0; j < m; j++) {
            std::cin >> a >> b;
            for (int k = 0; k < b; k++) {
                int tmp = v.size();
                for (int l = 0; l < tmp; l++) {
                    v.push_back(v[l]*a);
                }
            }
        }
        v.erase(std::unique(v.begin(), v.end()), v.end());

        for (int k = 0; k < v.size(); k++) {
            for (int l = k; l < v.size(); l++) {
                if (lcm(v[k],v[l]) == v[v.size()-1]) {
                    std::cout << "TEST " << k << "  " << l << "  " << v[k] << "  " << v[l] <<std::endl;
                    r += v[k] + v[l];
                }
            }
        }
        std::cout << "Case " << i+1 << ": "  << r << std::endl;
    }
}