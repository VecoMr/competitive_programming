#include <iostream>
#include <vector>
#include <algorithm>

#define IS_LOWER(a) ('a' <= (a) && (a) <= 'z')
#define TO_LOWER(a) (IS_LOWER((a)) ? (a) : ((a) + ('a' - 'A')))

bool sort_vector(std::string a, std::string b)
{
    int i = 0;
    for (i; i < a.size() && a[i] == b[i]; i++);
    if (TO_LOWER(a[i]) == TO_LOWER(b[i])) {
        // std::cout << "SORT " << a << "  " << b << "  " << (int) (a[i] < b[i]) << "  " << i << "  " << 1 << std::endl;
        return a[i] < b[i];
    } else {
        // std::cout << "SORT " << a << "  " << b << "  " << (int)(TO_LOWER(a[i]) < TO_LOWER(b[i])) << "  " << i << "  " << 2 << std::endl;
        return TO_LOWER(a[i]) < TO_LOWER(b[i]);
    }
}

int main()
{
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::string str;
        std::vector <std::string> vec;
        std::cin >> str;
        std::sort(str.begin(), str.end());
        do {
            vec.push_back(str);
            // std::cout << "Perm " << str << std::endl;
        } while(std::next_permutation(str.begin(), str.end()));
        std::sort(vec.begin(), vec.end(), sort_vector);
        for (auto &a: vec) {
            std::cout << a << std::endl;
        }
    }
}