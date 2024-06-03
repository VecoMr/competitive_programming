#include <iostream>

int main(void)
{
    int a,b;
    std::cin >> a >> b;
    int i = 0;
    while (a > b) {
        if (a % 2 != 0) {
            i++;
            a++;
        }
        if (a % 2 == 0) {
            a /= 2;
            i++;
        }
    }
    std::cout << b-a+i << std::endl;
}