#include <iostream>

int main(void)
{
    long int b = 0;
    long int p = 0;
    long int m = 0;

    while (std::cin >> b && std::cin >> p && std::cin >> m) {
        long int r = 1;
        long int tmp = b;
        // std::cout << "b = " << b << " p = "<< p << " m = " << m << std::endl;
        while (p > 0) {
            if (p%2 == 1) {
                r = (r*tmp) % m;
            }
            tmp = (tmp*tmp) % m;
            p /= 2;
        }
        std::cout << r << std::endl;
    }
}