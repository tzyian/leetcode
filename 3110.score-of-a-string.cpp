// @leet start
#include <string>
using std::string;


class Solution {
public:
    int scoreOfString(string s) {
        int sum = 0;
        int prev = s[0];
        for (int i = 1; i < s.size(); ++i) {
            sum += std::abs(s[i] - prev);
            prev = s[i];
        }
        return sum;
    }
};
// @leet end
