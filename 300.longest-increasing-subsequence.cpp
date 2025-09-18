#include <vector>
using std::vector;

// @leet start
class Solution {
  public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        int ans = 1;
        vector<int> dp(n + 1, 1);
        // dp[i] is the length of LIS ending with nums[i-1]
        // and dp[0] is an empty sequence
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j < i; ++j) {
                if (nums[i - 1] > nums[j - 1]) {
                    dp[i] = std::max(dp[i], 1 + dp[j]);
                    ans = std::max(ans, dp[i]);
                }
            }
        }
        return ans;
    }
};

// @leet end
