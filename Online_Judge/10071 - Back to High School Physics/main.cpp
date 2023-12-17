#include <iostream>

int main(void)
{
    int v = 0;
    int t = 0;

    while (std::cin >> v >> t) {
        std::cout << v*t*2 << std::endl;
    }
}