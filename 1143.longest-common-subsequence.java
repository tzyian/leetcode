
// @leet imports start
import java.util.*;
import java.math.*;
// @leet imports end

// @leet start
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {

        if (text1.length() < text2.length()) {
            String temp = text1;
            text1 = text2;
            text2 = temp;
        }
        int n = text1.length();
        int m = text2.length();

        int[] dp = new int[n + 1];
        for (int i = 1; i <= m; i++) {
            int prevRowPrevCol = 0;
            for (int j = 1; j <= n; j++) {
                int prevRow = dp[j];
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[j] = 1 + prevRowPrevCol;
                } else {
                    dp[j] = Math.max(dp[j], dp[j - 1]);
                }
                prevRowPrevCol = prevRow;
            }

        }

        return dp[n];

    }
}
// @leet end
