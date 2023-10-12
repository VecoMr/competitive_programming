#include <vector>
#include <iostream>

int main(void) {
    int n, m;
    while (true) {
        std::cin >> n >> m;
        if (m == 0 && n == 0) break;
        std::vector<std::vector<int> > appel;
        int s, d, c, t;
        for (int i = 0; i < n; i++) {
            std::cin >> s >> d >> c >> t;
            std::vector<int> tmp;
            tmp.push_back(c);
            tmp.push_back(t);
            appel.push_back(tmp);
        }
        for (int i = 0; i < m; i++) {
            std::cin >> c >> t;
            int r = 0;
            for (int j = 0; j < n; j++) {
                s = appel[j][0];
                d = appel[j][1];
                if ((c < s && s < c+t) || (c < s+d && s+d < c+t) || (s < c && c < s+d) || (s < c+t && c+t < s+d) || (s == c && s+d == c+t)) {
                    r++;
                }
            }
            std::cout << r << std::endl;
        }
    }
}