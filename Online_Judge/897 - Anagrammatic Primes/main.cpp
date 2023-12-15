#include <bitset>
#include <iostream>
#include <algorithm>
#include <vector>

void sieve(long long ub, std::bitset<10000010> &bs)
{
    long long size = ub+1;
    for (int i = 2; i < size; i++) {
        if (!bs[i]) continue;
        for (int j = i*2; j < size; j += i) bs[j] = 0;
    }
}


int main(void)
{
    int n = 0;
    std::bitset<10000010> bs;
    while (std::cin >> n && n) {
        bs.set();
        bs[0] = bs[1] = 0;
        long long upper = 1;
        while (upper <= n) upper *= 10;
        sieve(upper, bs);
        bool tmp = true;
        while (tmp && n < upper) {
            std::string str = std::to_string(++n);
            std::sort(str.begin(), str.end());
            tmp = false;
            do {
                int t = std::stoi(str);
                if (bs[t] == 0) {
                    tmp = true;
                    break;
                }
            } while (std::next_permutation(str.begin(), str.end()));
            if (!tmp) {
                std::cout << n << std::endl;
            }
        }
        if (tmp) {
            std::cout << 0 << std::endl;
        }
    }
}