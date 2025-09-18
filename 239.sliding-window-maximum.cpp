#include <vector>
using std::vector;
#include <deque>
using std::deque;

// @leet start
class Solution {
  public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        // O(n) TC from iteration
        // O(n) SC from deque
        // basically a monotonic queue where the front is always the largest

        deque<int> dq;
        vector<int> ans;
        auto n = nums.size();

        for (auto i = 0; i < n; ++i) {
            // remove all out of range elements in the front
            while (!dq.empty() && dq.front() <= i - k) {
                dq.pop_front();
            }
            // remove smaller numbers than current number
            // since curr number will be chosen rather than smaller numbers
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }

            dq.push_back(i);

            if (i >= k - 1) {
                ans.push_back(nums[dq.front()]);
            }
        }

        return ans;
    }
};
// @leet end
