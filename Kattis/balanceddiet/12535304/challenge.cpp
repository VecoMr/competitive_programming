#include <iostream>
#include <vector>

int main(void)
{
    int n = 0;
    while (std::cin >> n && n) {
        std::vector<int> v(n);
        int sum = 0;
        for (int i = 0; i < n; i++) {
            std::cin >> v[i];
            sum += v[i];
        }
        int target = sum/2;
        std::vector<bool> dp(target+1, false);
        dp[0] = true;
        for (int j = 0; j < n; j++) {
            for (int i = target; i > 0; i--) {
                if (i - v[j] >= 0) {
                    if (dp[i-v[j]])
                        dp[i] = true;
                }
            }
        }
        int i = target;
        for (i = target; i >= 0 && dp[i] == false; i--);
        std::cout << sum - i << " " << i<< std::endl;
    }
}