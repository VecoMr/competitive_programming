#include <iostream>

int main() {
    int x, y = 0;
    while (std::cin >> x >> y) {
        int max = 0;
        int min = 0;
        if (x > y) {
            max = x;
            min = y;
        } else {
            max = y;
            min = x;
        }
        int maxCycle = 0;
        for (int i = min; i <= max; i++) {
            int cycle = 1;
            int n = i;
            while (n != 1) {
                if (n % 2 == 0) {
                    n /= 2;
                } else {
                    n = 3 * n + 1;
                }
                cycle++;
            }
            if (cycle > maxCycle) {
                maxCycle = cycle;
            }
        }
        std::cout << x << " " << y << " " << maxCycle << std::endl;
    }
}