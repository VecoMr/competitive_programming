#include <iostream>
#include <algorithm>

int main(void)
{
    int n;
    std::cin >> n;
    std::string v = "aeiou";
    std::string c = "bcdfghjklmnpqrstvwxyz";
    std::string tmp = "     ";

    for (int i = 0; n > 0 && i < 5; i++) {
        tmp[0] = v[i];
        for (int j = 0; n > 0 && j < 21; j++) {
            tmp[1] = c[j];
            for (int k = 0; n > 0 && k < 21; k++) {
                tmp[2] = c[k];
                    for (int l = 0; n > 0 && l < 5; l++) {
                        tmp[3] = v[l];
                        for (int m = 0; n > 0 && m < 21; m++, n--) {
                            tmp[4] = c[m];
                            std::cout << tmp << std::endl;
                        }
                    }
            }
        }
    }
}
