// @leet start

import java.util.Arrays;

class Solution {
    public int partitionArray(int[] nums, int k) {
        Arrays.sort(nums);
        int ans = 0;
        int i = 0;
        int n = nums.length;
        while (i < n) {
            ans++;
            int curr = nums[i];
            while (i < n && nums[i] - curr <= k) {
                i++;
            }
        }

        return ans;

    }
}
// @leet end
