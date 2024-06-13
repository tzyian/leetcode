// @leet start
#include <string>
using std::string;

class Solution {
public:
    int appendCharacters(string s, string t) {
        int currChecking = 0;
        int remaining = t.size();
        for (const auto& c : s) {
            if (c == t[currChecking]) {
                remaining--;
                currChecking++;
            }
        }
        return remaining;
        
    }
};
// @leet end
