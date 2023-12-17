#include <iostream>

int main(void)
{
    double a = 0;
    char tmp = 0;
    double b = 0;
    int nb = 0;

    while (std::cin >> a >> tmp >>b) {
        nb++;
        double first = a/b*200;
        double second = 200 - first;
        if (a/b*200 > 200 ) {
            first = b/a*200;
            second = 200 - first;
        }
        std::cout << "Case " << nb << ": " << first << " " << second << std::endl;
    }
}