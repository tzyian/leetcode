// @leet imports start
#include <bits/stdc++.h>
#include <numeric>
using namespace std;
// @leet imports end

// @leet start
class Solution {
  public:
    int maxRotateFunction(vector<int>& nums) {
        // TC O(n) once for each loop
        // SC O(1)
        long long sum = std::accumulate(nums.begin(), nums.end(), 0);

        long long curr = 0;
        auto n = nums.size();
        for (int i = 0; i < n; ++i) {
            curr += nums[i] * i;
        }
        long long ans = curr;
        for (int i = n - 1; i >= 0; --i) {
            curr = curr + sum - n * nums[i];
            ans = max(curr, ans);
        }
        return ans;
    }
};
// @leet end
