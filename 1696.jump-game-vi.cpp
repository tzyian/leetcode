// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
  public:
    // Using a treeset runs in O(n log k) time
    // The expected solution runs in O(n) time using a deque
    // i.e. 239. Sliding Window Maximum
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n);
        multiset<int> ms;
        ms.insert(nums[0]);
        dp[0] = nums[0];
        for (int i = 1; i < n; ++i) {
            auto it = ms.rbegin(); // add largest
            dp[i] = nums[i] + *it;

            ms.insert(dp[i]);
            if (ms.size() > k) {
                ms.erase(ms.find(dp[i - k]));
            }
        }
        return dp[n - 1];
    }
};
// @leet end
