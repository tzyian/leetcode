// @leet start
#include <string>
#include <unordered_map>
using std::string;

class Solution {
public:
    int longestPalindrome(string s) {
        std::unordered_map<char, int> map;
        int length = 0;
        int numOdds = 0;
        for (const auto& c : s) {
            if (map[c] == 0 && numOdds == 0) {
                map[c]++;
                numOdds++;
            } else if (map[c] == 0 && numOdds > 0) {
                map[c]++;
                numOdds++;
            } else if (map[c] == 1 && numOdds > 0) {
                map[c] = 0;
                length += 2;
                numOdds--;
            } else {
                // should not happen, eg
                // map[c] == 1 && numOdds == 0
                length -= 100000;
            }
        }
        if (numOdds > 0) {
            length++;
        }
        return length;
    }
};
// @leet end
