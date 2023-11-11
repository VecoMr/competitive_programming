#include <iostream>

int main(void)
{
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        int l, w, h;
        std::cin >> l >> w >> h;
        if (l > 20 or w > 20 or h > 20) {
            std::cout << "Case " << i+1 << ": " << "bad" << std::endl;
        } else {
            std::cout << "Case " << i+1 << ": " << "good" << std::endl;
        }
    }
}