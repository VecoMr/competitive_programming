#include <iostream>

bool verif(std::string str)
{
    int len = str.length();
    for (int i = 0; i < len/2; i++) {
        if (str[i] != len - i - 1)
            return false;
    }
    return true;
}

int e(std::string str, int len) {
    if (len == 1) {
        return 1;
    }
    int res = 0;
    if (verif(str))
        res++;
    res += e(str.substr(0, len -1), i+1);
    res += e(str.substr(len-i-1, i+1), i+1);
    return res;
}

int main(void)
{
    std::string str;

    while (std::cin >> str) {
        int res = e(str, str.length());
        std::cout << res << std::endl;
    }
}