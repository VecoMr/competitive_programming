#include <iostream>

int main(void)
{
    int n = 0;
    std::cin >> n;
    int c = 0;
    for (int i = n/2; i > 0; i--) {
        c = c + 1;
        if (n % i == 0) {
            break;
        }
    }
    std::cout << c+n-n/2-1 << std::endl;
}