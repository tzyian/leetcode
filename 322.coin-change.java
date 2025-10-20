import java.util.Arrays;

// @leet start
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        dp[0] = 0;
        Arrays.sort(coins);
        for (int i = 1; i <= amount; i++) {
            dp[i] = Integer.MAX_VALUE;
            for (int c : coins) {
                if (i - c < 0) {
                    continue;
                }
                if (dp[i - c] == Integer.MAX_VALUE) {
                    continue;
                }
                dp[i] = Math.min(dp[i - c] + 1, dp[i]);
            }
        }
        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }
}
// @leet end
