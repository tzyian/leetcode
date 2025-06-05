#include <queue>
using std::priority_queue;
#include <string>
using std::string;
#include <unordered_map>
using std::unordered_map;
#include <vector>
using std::vector;

// @leet start
class Solution {
    // template from
    // https://leetcode.com/problems/lexicographically-smallest-equivalent-string/solutions/3047517/python3-union-find-template-explanations/
  private:
    unordered_map<char, char> uf;

    char find(char x) {
        if (!this->uf.contains(x)) {
            uf[x] = x;
        }
        if (x != uf[x]) {
            uf[x] = find(uf[x]);
        }
        return uf[x];
    }

    void unite(char x, char y) {
        auto rootX = find(x);
        auto rootY = find(y);
        if (rootX < rootY) {
            this->uf[rootY] = rootX;
        } else {
            this->uf[rootX] = rootY;
        }
    }

  public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        for (auto i = 0; i < s1.size(); ++i) {
            unite(s1[i], s2[i]);
        }

        auto m = baseStr.size();
        char c;
        string s;
        s.reserve(m);
        for (auto i = 0; i < m; ++i) {
            c = find(baseStr[i]);
            s += c;
        }
        return s;
    }
};
// @leet end
