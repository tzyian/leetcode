#include <algorithm>
#include <climits>
#include <vector>

using std::vector;

// The problem with doing front-- and back++ 
// if nums[back-1]-nums[front] > nums[back]-nums[front+1]
// is you don't know whether to do front++ or back-- for either case
//
// The problem with comparing front 3 and back 3 is 
// 00 09 18 27 100 110 120 130
// best is delete last 3
//
// d1 = 10 - 0 = 10
// d2 = 14 - 1 = 13
// go back
//
//
// 1 2 3 4 5
// Theoretically faster if you in place quickselect smallest 4 and largest 4 in O(n) TC O(1) SC,
// then sort the 2 tails, then compare the 2 tails, O(t) where t is length of each tail
// As it turns out C++ has std::partial_sort and std::nth_element which does that for you

// @leet start
class Solution {
public:
    int minDifference(vector<int>& nums) {
        int n = nums.size();
        if (n <= 4) {
            return 0;
        }
        std::sort(nums.begin(), nums.end());
        int minDiff = INT_MAX;
        for (int i = 0; i < 4; ++i) {
            minDiff = std::min(minDiff, nums[n - 4 + i] - nums[i]);
        }
        return minDiff;
    }
};
// @leet end
