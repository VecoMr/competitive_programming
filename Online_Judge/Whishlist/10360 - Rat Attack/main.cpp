#include <vector>
#include <iostream>

int calc(int x, int y, int d, std::vector<std::vector<int> > v)
{
    int r = 0;
    for (int i = 0; i < v.size(); i++) {
        if (x-d <= v[i][0] && x+d >= v[i][0] && y-d <= v[i][1] && y+d >= v[i][1]) {
            r += v[i][2];
        }
    }
    return r;
}

int main(void)
{
    int n = 0;
    int m = 0;
    int d = 0;
    int a,b,c = 0;
    std::cin >> n;
    int x, y, ma = 0;
    std::vector<std::vector<int> > v;

    for (int i = 0; i < n; i++) {
        int x_min, x_max = 0;
        int y_min, y_max = 0;
        v.clear();
        std::cin >> d;
        std::cin >> m;
        // std::cout << "test : " << d << "  " << m << std::endl;
        for (int j = 0; j < m; j++) {
            std::vector<int> tmp;
            std::cin >> a >> b >> c;
            if (a < x_min)
                x_min = a;
            if (a > x_max)
                x_max = a;
            if (b < y_min)
                y_min = b;
            if (b > y_max)
                y_max = b;
            tmp.push_back(a);
            tmp.push_back(b);
            tmp.push_back(c);
            v.push_back(tmp);
        }
        // std::cout << "Vector" << std::endl;
        // for (int i = 0; i < v.size(); i++) {
        //     std::cout << v[i][0] << " " << v[i][1] << " " << v[i][2] << std::endl;
        // }

        // std::cout << "X min : " << x_min << " " << "X max : " << x_max << " "  << "Y min : " << y_min << " " << "Y max : " << y_max << std::endl;

        int tmp = 0;
        ma = 0;
        for (int k = x_min; k <= x_max; k++) {
            for (int l = y_min; l < y_max; l++) {
                tmp = calc(k, l, d, v);
                if (tmp > ma) {
                    ma = tmp;
                    x = k;
                    y = l;
                }
            }
        }
        char *test = new char[10];
        std::cin.getline(test, 5);
        std::cout << x << " " << y << " " << ma << std::endl;
        // std::cout << test << std::endl;
    }
}