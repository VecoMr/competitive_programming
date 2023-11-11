#include <vector>
#include <iostream>

bool issorted(std::vector<int> l)
{
    int tmp = 0;
    for (int i = 0; i < l.size(); i++) {
        if (l[i] < tmp)
            return false;
        tmp = l[i];
    }
    return true;
}

int main(void)
{
    int n = 0;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int m = 0;
        std::cin >> m;
        std::vector<int> l(m);
        for (int j = 0; j < m; j++)
            std::cin >> l[j];
        int res = 0;
        while (!issorted(l)) {
            for (int j = 1; j < m; j++) {
                if (l[j-1] > l[j]) {
                    l[j] = l[j] ^ l[j - 1];
                    l[j - 1] = l[j - 1] ^ l[j];
                    l[j] = l[j] ^ l[j - 1];
                    res++;
                }
            }
        }
        std::cout << "Optimal train swapping takes " << res << " swaps." << std::endl;
    }
}