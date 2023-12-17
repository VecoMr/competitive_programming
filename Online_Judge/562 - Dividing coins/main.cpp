#include <vector>
#include <iostream>

int main(void)
{
    int n = 0;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int m = 0;
        int su = 0;
        std::vector<int> l(m);
        int tmp = 0;
        std::cin >> m;
        for (int j = 0; j < m; j++) {
            std::cin >> tmp;
            su += tmp;
            l.push_back(tmp);
        }
        int target = su/2;
        std::vector<bool> dp(target+1, false);
        dp[0] = true;
        // std::cout << "test" << std::endl;
        for (int j = 0; j < m; j++) {
            // std::cout << j << " " << target << " " << l[j] << std::endl;
            for (int k = target; k > 0; k--) {
                if (k-l[j] >= 0 && dp[k-l[j]]) {
                    dp[k] = true;
                }
            }
        }
        // std::cout << "test" << std::endl;

        for (int j = target; j > -1; j--) {
            if (dp[j]) {
                std::cout << su - j*2 << std::endl;
                break;
            }
        }

    }
}