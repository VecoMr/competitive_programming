#include <iostream>
#include <vector>

int main(void) {
    long long a = 0;
    long long b = 0;
    std::cin >> a >> b;
    long long ind = 1;
    while (a || b) {
        std::vector<long long> dp(a+1, 0);
        for (long long i = 2; i < a+1; i++) {
            dp[i] = (dp[i-1]+dp[i-2]+2)%b;
        }
        std::cout << "Case " << ind++ << ": " << a << " " << b << " " << (dp[a]+1)%b << std::endl;
        std::cin >> a >> b;
    }

}