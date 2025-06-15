#include <algorithm>
#include <vector>
using std::vector;

// @leet start
class Solution {
  public:
    int minimizeMax(vector<int>& nums, int p) {
        // solution is to do greedy iteration between every consecutive pair
        // then binary search across the min and max
        int n = nums.size();
        if (p == 0 || n <= 1) {
            // edge case
            return 0;
        }

        std::sort(nums.begin(), nums.end());
        // note that array is sorted, not differences
        int maxDiff = nums[n - 1] - nums[0];

        int lo = 0;
        int hi = maxDiff;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (isValid(nums, mid, p)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    bool isValid(vector<int>& nums, int threshold, int p) {
        // greedily count every consecutive pair of indices which are below
        // threshold skip index if the diff does not satisfy threshold
        int count = 0;
        int i = 1;
        while (i < nums.size()) {
            if (nums[i] - nums[i - 1] <= threshold) {
                ++count;
                ++i;
            }
            if (count == p) {
                return true;
            }
            ++i;
        }

        return false;
    }
};
// @leet end
