// @leet start
#include <vector>
#include <algorithm>
using std::vector;

class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        int total = 0;

        std::sort(nums.begin(), nums.end());
        int prev = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] < prev + 1) {
                total += prev + 1 - nums[i];
                ++prev;
            } else {
                prev = nums[i];
            }
        }
        return total;
        
    }
};
// @leet end
