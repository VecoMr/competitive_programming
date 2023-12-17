#include <iostream>
#include <vector>

bool isprime(int n)
{
    if (n == 2 || n == 3)
        return true;
    if (n < 2 or n % 2 == 0)
        return false;
    for (int i = 3; i < std::sqrt(0.5) + 1; i += 2) {
        if (n % i == 0)
            return false;
    }
    return true;
}

void solve(int )
{

}
