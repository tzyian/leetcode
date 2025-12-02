// @leet start
class Solution {
    public int maximumDifference(int[] nums) {
        int n = nums.length;
        int min = nums[0];
        int diff = -1;
        for (int i = 1; i < n; i++) {
            diff = Math.max(nums[i] - min, diff);
            min = Math.min(nums[i], min);
        }
        return diff > 0 ? diff : -1;

    }
}
// @leet end
