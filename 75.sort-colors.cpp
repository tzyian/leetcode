// @leet start
#include <vector>
using std::vector;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int i = 0;
        int j = 0;
        int k = nums.size() - 1;
        int mid = 1;

        while (j <= k) {
            if (nums[j] < mid) {
                swap(nums, i, j);
                ++i;
                ++j;
            } else if (nums[j] > mid) {
                swap(nums, j, k);
                --k;
            } else {
                ++j;
            }
        }
        
    }
private:
    void swap(vector<int>& nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
};
// @leet end
