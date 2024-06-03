#include <iostream>
#include <algorithm>
#include <memory>
#include <vector>

using namespace std;

class Node {
public:
    Node() :childs() {
        for (int i = 0; i < 10; i++)
            childs.emplace_back(nullptr);
    };
    ~Node() {};
    vector<unique_ptr<Node> > childs;
    bool add(string s, int k, int n) {
        if (k == n) {
            return false;
        }
        int t = s[k] - '0';
        if (childs[t] != nullptr) {
            return childs[t]->add(s, k+1, n);
        } else {
            childs[t] = std::unique_ptr<Node>(new Node());
            childs[t]->add(s, k+1, n);
            return true;
        }
        return false;
    };
};

struct compare {
    inline bool operator()(const std::string& first,
            const std::string& second) const
    {
        return first.size() > second.size();
    }
};

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        unique_ptr<Node> a(new Node());
        int m;
        cin >> m;
        bool tmp = true;
        vector<string> l(m);
        for (int j = 0; j < m; j++)
            cin >> l[j];
        compare c;
        std::sort(l.begin(), l.end(), c);
        for (int j = 0; j < m; j++) {
            if (!a->add(l[j], 0, l[j].size())) {
                tmp = false;
                break;
            }
        }
        if (tmp)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}