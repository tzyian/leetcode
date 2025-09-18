#include <vector>
using std::vector;

// @leet start
class Solution {
  public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        // This is actually exactly the same as LCS
        // Because a subseq removes indexes in between
        // And here unconnected values are also removed
        //
        // i.e.
        // best of (i,j) is 1 + (i-1,j-1) if equals,
        // else best of (i-1,j) and (i,j-1)
        int n = nums1.size();
        int m = nums2.size();

        vector<vector<int>> dp(n + 1, vector<int>(m + 1));
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[n][m];
    }
};
// @leet end
