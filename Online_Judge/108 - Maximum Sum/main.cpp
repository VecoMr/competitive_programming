#include <iostream>
#include <vector>
#include <climits>

int main(void)
{
    int n = 0;

    while (std::cin >> n) {
        std::vector<std::vector<int> > arr;
        std::vector<int> v;
        int x = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                std::cin >> x;
                v.push_back(x);
                if (v.size() == n) {
                    arr.push_back(v);
                    v.clear();
                }
            }
        }
        int r = INT_MIN;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                std::vector<int> k(n,0);
                std::vector<int> sum(n,0);

                for (int y = i; y < n; y++) {
                    for (int x = j; x < n; x++) {
                        k[x] += arr[y][x];
                        sum[x] = k[x];

                        if (x > 0)
                            sum[x] += sum[x-1];
                        if (sum[x] > r)
                            r = sum[x];
                    }
                }
            }
        }
        std::cout << r << std::endl;
    }
}