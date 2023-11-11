#include <iostream>

int main(void)
{
    int n = 0;
    std::cin >> n;
    int a = 0;
    int b = 0;
    for (int i = 0; i < n; i++) {
        std::cin >> a >> b;
        if (a < b) {
            std::cout << "<" << std::endl;
        } else if (a > b) {
            std::cout << ">" << std::endl;
        } else {
            std::cout << "=" << std::endl;
        }
    }
}