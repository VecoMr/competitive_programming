#include <iostream>
#include <vector>


int main(void)
{
    int n, m = 0;
    std::string tmp = "";
    std::vector <std::string> dieux;

    std::cin >> n;
    for (int i = 0; i < n; i++, std::cin >> tmp, dieux.push_back(tmp));

    std::cin >> m;
    std::string first_name, first_last, second_name, second_last = "";
    std::vector<int> mat_possible;
    std::vector<int> mat;
    for (int i = 0; i < m; i++) {
        std::cin >> first_name >> first_last >> second_name >> second_last;
        std::string f = first_name + first_last;
        std::string s = second_name + second_last;
        
    }
}