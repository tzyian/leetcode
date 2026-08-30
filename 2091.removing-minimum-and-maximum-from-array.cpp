// @leet imports start
#include "debug.hpp"
#include <climits>
using namespace std;
// @leet imports end

// @leet start
class Solution {
  public:
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();
        int vmin = INT_MAX, min_idx = 0, vmax = INT_MIN, max_idx = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] < vmin) {
                vmin = nums[i];
                min_idx = i;
            }
            if (nums[i] > vmax) {
                vmax = nums[i];
                max_idx = i;
            }
        }
        int mins = std::min(min_idx, max_idx);
        int maxs = std::max(min_idx, max_idx);
        int del_from_front = maxs + 1;
        int del_from_back = n - mins;
        int del_separate = mins + 1 + n - maxs;
        return min({del_separate, del_from_front, del_from_back});
    }
};
// @leet end
