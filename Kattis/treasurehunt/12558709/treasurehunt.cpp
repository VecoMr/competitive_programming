#include <iostream>
#include <vector>

int main(void)
{
    int r, c;
    std::cin >> r >> c;
    std::vector<std::string> map(r);
    for (int i = 0; i < r; i++)
        std::cin >> map[i];
    std::vector<std::vector<bool> > mem(r, std::vector<bool> (c, 0));
    int x = 0, y = 0;
    int nb = 0;
    while (map[y][x] != 'T') {
        nb++;
        switch (map[y][x])
        {
            case 'E':
                x++;
                break;
            case 'W':
                x--;
                break;
            case 'N':
                y--;
                break;
            case 'S':
                y++;
                break;
            default:
                break;
        }
        if (x >= c || x < 0 || y >= r || y < 0) {
            std::cout << "Out" << std::endl;
            return 0;
        }
        if (mem[y][x]) {
            std::cout << "Lost" << std::endl;
            return 0;
        }
        mem[y][x] = 1;
        
    }
    std::cout << nb << std::endl;
}