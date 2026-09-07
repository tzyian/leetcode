// @leet imports start
#include "debug.hpp"
using namespace std;
// @leet imports end

// @leet start
class Solution {
  public:
    int numDistinct(string s, string t) {
        int n = s.size();
        int m = t.size();
        // dp[i][j] = number of ways
        // using the s[:i]
        // to form the prefix string t[:j]
        auto dp = vector(n + 1, vector<unsigned long long>(m + 1));
        // 1 way to form "" using s
        for (int i = 0; i <= n; ++i) {
            dp[i][0] = 1;
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        return dp[n][m];
    }
};
// @leet end
int main() {
    Solution s;
    string s1 = "babgbag";
    string s2 = "bag";
    // string s1 = "rabbbit";
    // string s2 = "rabbit";
    auto out = s.numDistinct(s1, s2);
    debug(out);
}
