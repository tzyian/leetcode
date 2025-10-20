
// @leet imports start
import java.util.*;
import java.math.*;
// @leet imports end

// @leet start
class Solution {
    public int maxArea(int[] height) {
        int n = height.length;
        int l = 0;
        int r = n - 1;
        int ans = 0;
        while (l < r) {
            int hl = height[l];
            int hr = height[r];
            int water = Math.min(hl, hr) * (r - l);
            ans = Math.max(ans, water);
            if (hl < hr) {
                l++;
            } else {
                r--;
            }
        }
        return ans;

    }
}
// @leet end
