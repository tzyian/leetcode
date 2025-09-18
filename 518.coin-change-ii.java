
// @leet imports start
import java.util.*;
import java.math.*;
// @leet imports end

// @leet start
class Solution {
    public int change(int amount, int[] coins) {
        // dp[i][j] is number of ways to make $i using the first j coins
        int m = coins.length;
        int[][] dp = new int[amount + 1][m + 1];
        dp[0][0] = 1;

        for (int j = 0; j <= m; j++) {
            dp[0][j] = 1;
        }

        for (int i = 1; i <= amount; i++) {
            for (int j = 1; j <= m; j++) {

                int use;
                int notUse = dp[i][j - 1];
                if (i >= coins[j - 1]) {
                    use = dp[i - coins[j - 1]][j];
                } else {
                    use = 0;
                }
                dp[i][j] = use + notUse;

            }
        }
        return dp[amount][m];

    }
}
// @leet end
