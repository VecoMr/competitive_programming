#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>

int main(void)
{
    int n = 0;
    int m = 0;
    int direction = 1;

    std::cin >> n >> m;
    std::list<std::string> villes(n);
    std::list<std::string> mangees{};
    std::for_each(villes.begin(), villes.end(), [](std::string &ville) { std::cin >> ville; });
    std::string actions;
    std::cin >> actions;

    std::list<std::string>::iterator current = villes.begin();

    for (const auto &action: actions) {
        switch (action) {
            case 'A':
                if (direction > 0) {
                    current++;
                    if (current == villes.end())
                        current = villes.begin();
                } else {
                    if (current == villes.begin())
                        current = villes.end();
                    current--;
                }
                break;
            case 'M':
                mangees.push_back(*current);
                if (direction > 0) {
                    auto tmp = current;
                    current++;
                    if (current == villes.end())
                        current = villes.begin();
                    villes.erase(tmp);
                } else {
                    auto tmp = current;
                    if (current == villes.begin())
                        current = villes.end();
                    current--;
                    villes.erase(tmp);
                }
                break;
            case 'R':
                if (direction > 0) {
                    if (current == villes.begin())
                        current = villes.end();
                    current--;
                } else {
                    current++;
                    if (current == villes.end())
                        current = villes.begin();
                }
                direction *= -1;
                break;
            case 'C':
                if (direction > 0) {
                    current = villes.insert(current, mangees.back());
                    mangees.pop_back();
                } else {
                    current = villes.insert(++current, mangees.back());
                    mangees.pop_back();
                }
                break;
        }
    }

    for (int i = 0; i < villes.size(); i++) {
        std::cout << *current << std::endl;
        if (direction > 0) {
            current++;
            if (current == villes.end())
                current = villes.begin();
        } else {
            if (current == villes.begin())
                current = villes.end();
            current--;
        }
    }
    return 0;
}
