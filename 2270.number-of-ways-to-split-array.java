// @leet start
class Solution {
    public int waysToSplitArray(int[] nums) {
        int n = nums.length;

        long ssum = 0;
        for (int num : nums) {
            ssum += num;
        }

        int ans = 0;
        long psum = 0;

        for (int i = 0; i < n - 1; i++) {
            ssum -= nums[i];
            psum += nums[i];
            if (psum >= ssum) {
                ans++;
            }
        }

        return ans;

    }
}
// @leet end
