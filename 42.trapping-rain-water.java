
// @leet start
class Solution {
    // 2 pointers version by moving right leftwards and left rightwards
    // O(n) TC
    // O(1) SC
    public int trap(int[] height) {
        int n = height.length;

        if (n <= 1) {
            return 0;
        }

        int water = 0;
        int l = 0;
        int r = n - 1;
        int maxLeft = height[0];
        int maxRight = height[n - 1];

        while (l <= r) {
            if (maxLeft < maxRight) {
                if (height[l] > maxLeft) {
                    maxLeft = height[l];
                } else {
                    water += maxLeft - height[l];
                }
                l += 1;
            } else {
                if (height[r] > maxRight) {
                    maxRight = height[r];
                } else {
                    water += maxRight - height[r];
                }
                r -= 1;

            }
        }
        return water;
    }

}
// @leet end
