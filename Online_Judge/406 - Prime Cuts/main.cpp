#include <bitset>
#include <vector>
#include <iostream>

void sieve(long long ub, std::bitset<10000010> bs, std::vector<long long> &primes)
{
    long long size = ub+1;
    for (int i = 2; i < size; i++) {
        if (!bs[i]) continue;
        for (int j = i; j < size; j += i) bs[j] = 0;
        primes.push_back(i);
    }
}

int main(void)
{
    std::bitset<10000010> bs;
    long long upperbounds = 1;
    long long n, m;
    long long nb = 0;
    while (std::cin >> n >> m) {
        bs.set();
        bs[0] = 0;
        bs[1] = 0;
        std::vector<long long> primes;
        primes.push_back(1);
        sieve(n, bs, primes);
        long long size = primes.size();
        if (nb++ > 0) {
            std::cout << std::endl;
        }
        std::cout << n << " " << m << ":";
        if (size < 2*m) {
            for (int j = 0; j < size; j++) {
                std::cout << " " << primes[j];
            }
        } else {
            if (size%2) {
                for (int j = size/2-m+1; j < size/2+m; j++) {
                    std::cout << " " << primes[j];
                }
            } else {
                for (int j = size/2-m; j < size/2+m; j++) {
                    std::cout << " " << primes[j];
                }
            }
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
    return 0;
}
