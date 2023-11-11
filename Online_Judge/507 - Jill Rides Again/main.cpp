#include <vector>
#include <iostream>

int main(void)
{
    int n = 0;
    int tmp = 0;
    std::cin >> n;

    for (int k = 0; k < n; k++) {
        int m = 0;
        int x = 1;
        int y = 1;
        int start = 1;
        int res = 0;
        int curr = 0;
        std::cin >> m;

        for (int i = 1; i < m; i++) {
            std::cin >> tmp;
            curr += tmp;
            if (curr < 0) {
                curr = 0;
                start = i + 1;
                // std::cout << "start = " << start << std::endl;
            }
            if (curr > res) {
                res = curr;
                x = start;
                y = i + 1;
                // std::cout << "i = " << i << " res = " << res << " x = " << x << std::endl;
            }
            if (curr == res && y-x < i+1-start) {
                x = start;
                y = i + 1;
            }
        }
        if (res == 0) {
            std::cout << "Route " << k + 1 << " has no nice parts" << std::endl;
        } else {
            std::cout << "The nicest part of route " << k+1 << " is between stops " << x << " and " << y << std::endl;
        }
        // std::cout << res << "  " << x << "  " << y << std::endl;
    }
}