#include <algorithm>
#include <iostream>
#include <vector>

bool is_possible(std::vector<std::vector<int> > v, std::vector<int> people)
{
    std::vector<int> tmp;
    for (int i = 0; i < people.size(); i++)
        tmp.push_back(0);
    for (int i = 0; i < people.size(); i++)
        tmp[people[i]] = i;
    for (int i = 0; i < v.size(); i++) {
        if (v[i][2] < 0) {
            if (std::abs(tmp[v[i][0]]-tmp[v[i][1]]) < std::abs(v[i][2]))
                return false;
        } else {
            if (std::abs(tmp[v[i][0]]-tmp[v[i][1]]) > v[i][2])
                return false;
        }
    }
    return true;
}

int main(void)
{
    int n, m, r;

    while (std::cin >> n >> m) {
        r = 0;
        if (n == 0 and m == 0)
            break;
        std::vector<std::vector<int> > v;
        std::vector<int> people;
        for (int i = 0; i < n; i++)
            people.push_back(i);
        for (int i = 0; i < m; i++) {
            std::vector<int> tmp;
            int a, b, c;
            std::cin >> a >> b >>c;
            tmp.push_back(a);
            tmp.push_back(b);
            tmp.push_back(c);
            v.push_back(tmp);
        }
        do {
            if (is_possible(v, people))
                r++;
        } while(std::next_permutation(people.begin(), people.end()));
        std::cout << r << std::endl;
    }
}