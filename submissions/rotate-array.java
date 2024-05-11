// https://leetcode.com/problems/rotate-array

class Solution {
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        if (len <= 1) {
            return;
        }

        k %= len;
        this.reverse(nums, 0, len - 1);
        this.reverse(nums, 0, k - 1);
        this.reverse(nums, k, len - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}