// @leet imports start

import java.util.*;
import java.math.*;
// @leet imports end

// @leet start
class Solution {

    public boolean canPartition(int[] nums) {
        int sum = Arrays.stream(nums).sum();
        if ((sum & 1) != 0) {
            return false;
        }
        int n = nums.length;
        int half = sum / 2;

        // dp[j][i] means whether we can get sum j using first i numbers
        boolean[][] dp = new boolean[half + 1][n + 1];

        for (int i = 0; i <= n; i++) {
            dp[0][i] = true;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= half; j++) {
                dp[j][i] = dp[j][i - 1];
                if (j >= nums[i - 1]) {
                    dp[j][i] = dp[j][i] || dp[j - nums[i - 1]][i - 1];
                    // ........................................^
                    // i-1 to prevent reuse
                }
            }
        }
        return dp[half][n];

    }

}
// @leet end
//
// 6, 1, 1
