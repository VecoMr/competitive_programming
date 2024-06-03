#include <iostream>
#include <vector>

using namespace std;

// void fillWater(vector<vector<int> > &l, int x, int y, int n, int m)
// {
//     if (x >= m || x < 0 || y >= n || y < 0)
//         return;
//     cout << x << " " << y << endl;
//     for (auto &v: l) {
//         for (auto i: v) {
//             cout << i;
//         }
//         cout << endl;
//     }
//     if (l[y][x] == 0)
//         l[y][x] = 2;
//         fillWater(l, x+1, y, n, m);
//         fillWater(l, x-1, y, n, m);
//         // fillWater(l, x, y+1, n, m);
//         // fillWater(l, x, y-1, n, m);
//     cout << "no"<<endl;
//     return;
// }
void fillWater(vector<vector<int> > &l, int x, int y, int n, int m)
{
    if (x >= m || x < 0 || y >= n || y < 0 || l[y][x] != 0)
        return;
    l[y][x] = 2;
    fillWater(l, x+1, y, n, m);
    fillWater(l, x-1, y, n, m);
    fillWater(l, x, y+1, n, m);
    fillWater(l, x, y-1, n, m);
}

int main()
{
    int n, m;
    cin >> n >> m;
    vector<vector<int> > l(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        string tmp;
        cin >> tmp;
        for (int j = 0; j < m; j++)
            l[i][j] = tmp[j] - '0';
    }
    for (int i = 0; i < n; i++) {
        if (l[i][0] == 0)
            fillWater(l, 0, i, n, m);
        if (l[i][m-1] == 0)
            fillWater(l, m-1, i, n, m);
    }
    for (int i = 0; i < m; i++) {
        if (l[0][i] == 0)
            fillWater(l, i, 0, n, m);
        if (l[n-1][i] == 0)
            fillWater(l, i, n-1, n, m);
    }
    size_t r = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (l[i][j] == 1) {
                if (i - 1 < 0 || l[i-1][j] == 2) r+=1;
                if (i + 1 >= n || l[i+1][j] == 2) r+=1;
                if (j - 1 < 0 || l[i][j-1] == 2) r+=1;
                if (j + 1 >= m || l[i][j+1] == 2) r+=1;
            }
        }
    }
    cout << r << endl;
}