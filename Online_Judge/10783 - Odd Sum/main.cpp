#include <iostream>

int main(void)
{
    int n = 0;
    int a = 0;
    int b = 0;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int res = 0;
        std::cin >> a;
        std::cin >> b;
        for (int j = a + (a+1)%2; j <= b; j += 2) {
            res += j;
        }
        std::cout << "Case " << i+1 << ": " << res << std::endl;
    }
}