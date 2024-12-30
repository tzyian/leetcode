// @leet start
#include <numeric>
#include <vector>
using std::vector;

class Solution {
  public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        int totalSum = std::accumulate(nums.begin(), nums.end(), 0);

        if (target < -totalSum || target > totalSum) {
            return 0;
        }

        vector<int> dp(2 * totalSum + 1, 0);
        // NOTE: += 1 because if nums[0] == 0, there are 2 ways to reach it
        dp[nums[0] + totalSum] += 1;
        dp[-nums[0] + totalSum] += 1;

        for (int i = 1; i < n; ++i) {
            vector<int> next(2 * totalSum + 1, 0);

            // NOTE: j <= totalSum to check all states
            for (int j = -totalSum; j <= totalSum; ++j) {
                // must check that prev state j + totalSum is a valid state
                int prev = dp[j + totalSum];
                if (prev > 0) {
                    next[j + nums[i] + totalSum] += prev;
                    next[j - nums[i] + totalSum] += prev;
                }
            }
            dp = next;
        }
        return dp[target + totalSum];
    }
};
// @leet end
