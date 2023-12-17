#include <vector>
#include <iostream>

int main(void)
{
    std::string str;
    std::vector<char> q(str.size()+1, 0);
    int cursor = 0;

    std::cin >> str;

    for (int i = 0; i < str.size(); i++) {
        if (str[i] == '<') {
            q[cursor-1] = 0;
            cursor--;
        } else {
            q[cursor] = str[i];
            cursor++;
        }
    }
    for (int i = 0; i < cursor; i++) {
        std::cout << q[i];
    }
    std::cout << std::endl;
}